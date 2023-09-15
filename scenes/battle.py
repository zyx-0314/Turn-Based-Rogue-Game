import pygame
import random
import os

from utils import *
from components.ui import HealthBar
from components.buttons import Button
from components.characters import Player, Enemy
from stats.consumableStats import ConsumableStats

pygame.init()

screen = init_display()

draw = init_draw(screen)

background_img = load_and_transform_image.background_img("assets/background/dansel.jpg")
main_panel_img = load_and_transform_image.main_panel_img("assets/panels/main panel.png")

class BattleScene():
    def __init__(self, SelectedCharacter, SelectedEnemy):
        action_cooldown = 0
        current_fighter = "mc"
        action_wait_time = 120

        attack = False
        clicked = False

        bagButton = []
        skillButton = []
        statusEffect = []

        damage_text_group = pygame.sprite.Group()

        def addToArray(value, counter, type, array):
            img = load_and_transform_image.convert(f"assets/{value['type']}/{value['name'].lower()}.png")
            if type == "status":
                button = Button(screen, leftTextIndention + (40 * counter), 20, img, 32, 32, value['name'])
            elif type == "bag":
                button = Button(screen, leftTextIndention + (40 * counter), screen_height - bottom_panel + 70, img, 32, 32, value['name'])
            elif type == "skill":
                button = Button(screen, 220 + (40 * skillCounter), screen_height - bottom_panel + 30, img, 32, 32, value['name'])
            array.append(button)
            counter += 1

        mc = Player(200, groundLevel, damage_text_group, SelectedCharacter)
        enemy = Enemy(screen_width-200, groundLevel, damage_text_group, SelectedEnemy)

        presentCharacters = [mc, enemy]

        mc_health_bar = HealthBar(leftTextIndention, screen_height - bottom_panel + 40, mc.checkStat("curr hp"), mc.checkStat("max hp"))
        enemy_health_bar = HealthBar(rightTextIndention, screen_height - bottom_panel + 40, enemy.checkStat("curr hp"), enemy.checkStat("max hp"))

        skillCounter = 0
        for skills in ['attack1', 'focus']:
            addToArray({'name':skills, 'type':'skills'}, skillCounter, "skill", skillButton)
            skillCounter += 1

        counter = 0
        for items in mc.checkBag():
            addToArray(items, counter, "bag", bagButton)
            counter += 1

        running = True
        terminate = False
        while running:
            clock.tick(fps)

            draw.draw_bg(background_img)
            draw.draw_main_panel(main_panel_img)
            draw.draw_name(
                {"name": mc.checkName(), "hp": mc.checkStat("curr hp")},
                {"name": enemy.checkName(), "hp": enemy.checkStat("curr hp")}
            )

            mouse_pos = pygame.mouse.get_pos()

            if (current_fighter == "mc") & mc.checkIfAlive():
                attack = False

                for skill_button in skillButton:
                    if skill_button.draw():
                        if skill_button.name == "attack1":
                            mc.attack(enemy)
                        if skill_button.name == "focus":
                            mc.use_focus()
                        current_fighter = "enemy"

                for potion_button in bagButton:
                    if potion_button.draw():
                        mc.use_potion(ConsumableStats.PotionsStats(potion_button.name))
                        no_potion = True
                        for items in mc.checkBag():
                            if items['name'] == potion_button.name:
                                no_potion = False
                        if no_potion:
                            bagButton.remove(potion_button)


                statusEffect.clear()
                statusCounter = mc.checkStatusEffect().__len__() - 1
                for statusUpdate in mc.checkStatusEffect():
                    addToArray(statusUpdate, statusCounter, "status", statusEffect)
                    statusCounter -= 1

                if current_fighter == "enemy":
                    mc.status_ware_off()
                    bagButton.clear()
                    counter = 0
                    for items in mc.checkBag():
                        addToArray(items, counter, "bag", bagButton)
                        counter += 1

            for status in statusEffect:
                status.draw()

            if (current_fighter == "enemy") & enemy.checkIfAlive():
                action_cooldown += 1
                if action_cooldown >= action_wait_time:
                    action_cooldown = 0
                    enemy.attack(mc)
                    current_fighter = "mc"
                    turnDone = False

            for character in presentCharacters:
                character.update()
                character.draw(screen)

            mc_health_bar.draw(screen, mc.checkStat("curr hp"))
            enemy_health_bar.draw(screen, enemy.checkStat("curr hp"))

            damage_text_group.update()
            damage_text_group.draw(screen)

            if mc.checkIfAlive() == False or enemy.checkIfAlive() == False:
                if mc.checkIfAlive() == False:
                    draw.draw_text("You Lost!", font, red, screen_width/2 - 70, screen_height/2)

                if enemy.checkIfAlive() == False:
                    draw.draw_text("You Won!", font, green, screen_width/2 - 70, screen_height/2)

                icon = load_and_transform_image.scale(f"assets/icons/exit.png")
                button = Button(screen, screen_width/2 - 50, screen_height/2 + 50, icon, icon.get_width(), icon.get_height(), "OK")
                if button.draw():
                    return

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    terminate = True

            pygame.display.update()
        if terminate:
            pygame.quit()
