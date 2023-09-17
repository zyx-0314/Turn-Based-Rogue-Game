import pygame

from utils import *
from components.ui import HealthBar
from components.buttons import Button
from components.characters import Player, Enemy
from stats.consumableStats import ConsumableStats
from components.imageLoader import load_and_transform_image

screen = init_display()
draw = init_draw(screen)

background_img = load_and_transform_image.background_img("assets/background/dansel.jpg")
main_panel_img = load_and_transform_image.main_panel_img("assets/panels/main panel.png")

def addToArray(value, counter, type, array, maxCol=0, spacer=0):
    try:
        img = load_and_transform_image.convert(f"assets/{value['type']}/{value['file_icon'].lower()}.png")
        if type == "status":
            button = Button(
                screen, leftTextIndention + (50 * counter), 70, img, 32, 32, value['name'], f"{value['description']}"
            )
        elif type == "bag":
            button = Button(
                screen, rightTextIndention + (45 * counter), screen_height - bottom_panel + 30 + spacer, img, 32, 32, value['name'], f"{value['description']} - {value['turn']} turn"
        )
        elif type == "skill":
            button = Button(
                screen, leftTextIndention + (50 * counter), screen_height - bottom_panel + 30 + spacer, img, 32, 32, value['name'], f'{value["description"]} - {value["turn"]} turn'
            )
        array.append(button)
    except Exception as e:
        print(e, f'Current values {value} {counter} {type} {array} {maxCol} {spacer}')

def BattleScene(Player, SelectedEnemy):

    action_cooldown = 0
    current_fighter = "Player"
    action_wait_time = 120

    attack = False
    clicked = False

    bagButton = []
    skillButton = []
    statusEffect = []

    damage_text_group = pygame.sprite.Group()
    Player.setDamageTextGroup(damage_text_group)

    enemy = Enemy(screen_width-200, groundLevel, SelectedEnemy, damage_text_group)

    presentCharacters = [Player, enemy]

    mc_health_bar = HealthBar(leftTextIndention, 10, Player.checkStat("curr hp"), Player.checkStat("max hp"))
    enemy_health_bar = HealthBar(screen_width - 470, 10, enemy.checkStat("curr hp"), enemy.checkStat("max hp"))

    basic_attack = {
        "name": "Attack",
        "file_icon": "basic_attack",
        "description": "",
        "turn": 2,
        "type": "skills"
    }
    for index, skill in enumerate([basic_attack]+Player.checkSkills()):
        addToArray(skill, index, "skill", skillButton)

    for index, items in enumerate(Player.checkBag()):
        addToArray(items, index, "bag", bagButton)

    while True:
        clock.tick(fps)

        mouse_pos = pygame.mouse.get_pos()

        draw.draw_bg(background_img)
        draw.draw_main_panel(main_panel_img)

        draw.draw_name(
            {"name": Player.checkName(), "hp": Player.checkStat("curr hp")},
            {"name": enemy.checkName(), "hp": enemy.checkStat("curr hp")}
        )

        mc_health_bar.draw(screen, Player.checkStat("curr hp"))
        enemy_health_bar.draw(screen, enemy.checkStat("curr hp"))

        for status in statusEffect:
            status.draw()

        if (current_fighter == "Player") & Player.checkIfAlive():
            attack = False

            draw.draw_text("Skill", button_label_font, black, leftTextIndention, screen_height - bottom_panel + 10)

            for index, skill in enumerate(skillButton):
                
                if skill.rect.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, gray, skill.rect, 3)
                    draw.draw_text(skill.name, button_label_font, black, leftTextIndention + 40, screen_height - bottom_panel + 10)

                if skill.draw():
                    if skill.name == "Attack":
                        Player.attack(enemy)
                    else:
                        Player.use_skill(skill.name)
                    current_fighter = "enemy"

            draw.draw_text("Bag", button_label_font, black, rightTextIndention, screen_height - bottom_panel + 10)

            for index, item_button in enumerate(bagButton):

                if item_button.rect.collidepoint(mouse_pos):
                    pygame.draw.rect(screen, gray, item_button.rect, 3)
                    draw.draw_text(f'{item_button.name} - {item_button.description}', button_label_font, black, rightTextIndention + 30, screen_height - bottom_panel + 10)

                if item_button.draw():
                    Player.use_potion(ConsumableStats.PotionsStats(item_button.name))
                    no_potion = True
                    for items in Player.checkBag():
                        if items['name'] == item_button.name:
                            no_potion = False
                    if no_potion:
                        bagButton.remove(item_button)

            statusEffect.clear()
            for index, statusUpdate in enumerate(Player.checkStatusEffect()):
                addToArray(statusUpdate, index, "status", statusEffect)

            if current_fighter == "enemy":
                Player.status_ware_off()
                bagButton.clear()
                for index, items in enumerate(Player.checkBag()):
                    addToArray(items, index, "bag", bagButton)

        if (current_fighter == "enemy") & enemy.checkIfAlive():
            action_cooldown += 1
            if action_cooldown >= action_wait_time:
                action_cooldown = 0
                enemy.attack(Player)
                current_fighter = "Player"
                turnDone = False

        for character in presentCharacters:
            character.update()
            character.draw(screen)

        damage_text_group.update()
        damage_text_group.draw(screen)

        if Player.checkIfAlive() == False or enemy.checkIfAlive() == False:
            if Player.checkIfAlive() == False:
                draw.draw_text("You Lost!", font, red, screen_width/2 - 70, screen_height/2)

            if enemy.checkIfAlive() == False:
                draw.draw_text("You Won!", font, green, screen_width/2 - 70, screen_height/2)

            icon = load_and_transform_image.scale(f"assets/icons/exit.png")
            button = Button(screen, screen_width/2 - 50, screen_height/2 + 50, icon, icon.get_width(), icon.get_height(), "OK")
            if button.draw():
                return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'exit'

        pygame.display.update()
