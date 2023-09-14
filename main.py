import pygame
import random
import os

from utils import *
from components.buttons import *
from components.characters import *
from characterStats import *
from consumableStats import *

pygame.init()

screen = init_display()

background_img = load_and_transform_image.background_img("assets/background/dansel.jpg")
main_panel_img = load_and_transform_image.main_panel_img("assets/panels/main panel.png")

current_fighter = "mc"
action_cooldown = 0
action_wait_time = 90

attack = False
clicked = False

draw = init_draw(screen)

mc = Player(200, groundLevel, PlayerStat.Samurai)
enemy = Enemy(screen_width-200, groundLevel, MonsterStat.SoldierSkeleton)

mc_health_bar = HealthBar(leftTextIndention, screen_height - bottom_panel + 40, mc.hp, mc.max_hp)
enemy_health_bar = HealthBar(rightTextIndention, screen_height - bottom_panel + 40, enemy.hp, enemy.max_hp)

presentCharacters = [mc, enemy]

bagButton = []

itemCounter = 0
for items in mc.bag:
    potion_img = load_and_transform_image.convert(f"assets/potions/{items['name']}.png")
    potion_button = Button(screen, leftTextIndention + (40 * itemCounter), screen_height - bottom_panel + 70, potion_img, 32, 32, items['name'])
    bagButton.append(potion_button)
    itemCounter += 1

statusEffect = []

statusCounter = 0
for items in mc.status_effect:
    status_img = load_and_transform_image.convert(f"assets/potions/{items['name']}.png")
    status_button = Button(screen, leftTextIndention + (40 * statusCounter), screen_height - bottom_panel - 40, status_img, 32, 32, items['name'])
    statusEffect.append(status_button)
    statusCounter += 1

def addStatusEffect(status, counter):
    status_img = load_and_transform_image.convert(f"assets/potions/{status['name']}.png")
    status_button = Button(screen, leftTextIndention + (40 * counter), screen_height - bottom_panel - 40, status_img, 32, 32, status['name'])
    statusEffect.append(status_button)
    counter += 1

run = True
while run:
    clock.tick(fps)

    draw.draw_bg(background_img)
    draw.draw_panel(main_panel_img, draw.draw_text, mc, enemy)

    mouse_pos = pygame.mouse.get_pos()

    if (current_fighter == "mc") & mc.alive:
        attack = False

        if enemy.alive:
            if enemy.rect.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0] == 1 and clicked == False:
                    attack = True
                    clicked = True
            if pygame.mouse.get_pressed()[0] == 0:
                clicked = False

        for potion_button in bagButton:
            if potion_button.draw():
                mc.use_potion(ConsumableStats.PotionsStats(potion_button.name))
                no_potion = True
                for items in mc.bag:
                    if items['name'] == potion_button.name:
                        no_potion = False
                if no_potion:
                    bagButton.remove(potion_button)
                current_fighter = "enemy"

        if attack:
            mc.attack(enemy)
            current_fighter = "enemy"
        
        if current_fighter == "enemy":
            mc.status_ware_off()
            statusEffect.clear()
            statusCounter = mc.status_effect.__len__() - 1
            for statusUpdate in mc.status_effect:
                addStatusEffect(statusUpdate, statusCounter)
                statusCounter -= 1

    for status in statusEffect:
        status.draw()

    if current_fighter == "enemy":
        action_cooldown += 1
        if action_cooldown >= action_wait_time:
            action_cooldown = 0
            enemy.attack(mc)
            current_fighter = "mc"
            turnDone = False

    for character in presentCharacters:
        character.update()
        character.draw(screen)

    mc_health_bar.draw(screen, mc.hp)
    enemy_health_bar.draw(screen, enemy.hp)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
