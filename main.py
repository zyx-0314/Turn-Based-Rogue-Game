import pygame
import random
import os

from utils import *
from components.characters import *

pygame.init()

screen = init_display()

background_img = load_and_transform_image.background_img("assets/background/dansel.jpg")
main_panel_img = load_and_transform_image.main_panel_img("assets/panels/main panel.png")

current_fighter = "mc"
total_characters = 2
action_cooldown = 0
action_wait_time = 90

attack = False
clicked = False

draw = init_draw(screen)

mc = Samurai(200, groundLevel, "mc", 30, 10, 85)
skeleton = Enemy(screen_width-200, groundLevel, "skeleton", 200, 6, 85, 'potion')

mc_health_bar = HealthBar(leftTextIndention, screen_height - bottom_panel + 40, mc.hp, mc.max_hp)
enemy_health_bar = HealthBar(rightTextIndention, screen_height - bottom_panel + 40, skeleton.hp, skeleton.max_hp)

presentCharacters = [mc, skeleton]

run = True
while run:
    clock.tick(fps)

    draw.draw_bg(background_img)
    draw.draw_panel(main_panel_img, draw.draw_text, mc, skeleton)

    attack = False
    mouse_pos = pygame.mouse.get_pos()

    # check enemy is alive then check if mouse is clicked on enemy then attack the enemy
    if skeleton.alive & mc.alive & (current_fighter == "mc"):
        if skeleton.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1 and clicked == False:
                attack = True
                clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            clicked = False
        if attack == True:
            mc.attack(skeleton)
            current_fighter = "skeleton"

    if current_fighter == "skeleton":
        action_cooldown += 1
        if action_cooldown >= action_wait_time:
            action_cooldown = 0
            skeleton.attack(mc)
            current_fighter = "mc"

    for character in presentCharacters:
        character.update()
        character.draw(screen)

        # if character.alive & (current_fighter == character.name):
        #     action_cooldown += 1
        #     if action_cooldown >= action_wait_time:
        #         action_cooldown = 0
        #         character.attack(current_fighter == "mc" and skeleton or mc)
        #         current_fighter = current_fighter == "mc" and 'skeleton' or 'mc'
    mc_health_bar.draw(screen, mc.hp)

    enemy_health_bar.draw(screen, skeleton.hp)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
