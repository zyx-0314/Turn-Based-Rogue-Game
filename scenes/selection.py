import pygame
import random

from utils import *

from components.buttons import Button
from stats.characterStats import PlayerStat, MonsterStat

from scenes.battle import BattleScene

pygame.init()

screen = init_display()
draw = init_draw(screen)

background_img = load_and_transform_image.background_img("assets/background/dansel.jpg")
main_panel_img = load_and_transform_image.main_panel_img("assets/panels/main panel.png")

characterList = []

characterCounter = -1
for characters in ['samurai', 'archer']:
    character_img = load_and_transform_image.scale(f"assets/characters/{characters}/idle/0.png")
    character_button = Button(screen, screen_width/2+(200*characterCounter), groundLevel/2, character_img, character_img.get_width(), character_img.get_height(), characters)
    characterList.append(character_button)
    characterCounter += 1

def randomizeEnemy():
    enemies = [
      MonsterStat.SoldierSkeleton,
      MonsterStat.SpearmanSkeleton,
      MonsterStat.ArcherSkeleton,
    ]
    return random.choice(enemies)

def SelectionScene():
    running = True
    terminate = False
    while running:
        clock.tick(fps)

        draw.draw_bg(background_img)
        draw.draw_main_panel(main_panel_img)

        counter = 0
        for character in characterList:
            character.draw()
            draw.draw_text(character.name, font, green, screen_width/2 - 160 + (250*counter), groundLevel/2+80)
            counter += 1
        
        draw.draw_text("Select your character", font, white, screen_width/2 - 100, groundLevel/2-80)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for character in characterList:
                        if character.rect.collidepoint(event.pos):
                            if character.name == "samurai":
                                BattleScene(PlayerStat.Samurai, randomizeEnemy())
                            if character.name == "archer":
                                BattleScene(PlayerStat.Archer, randomizeEnemy())
            if event.type == pygame.QUIT:
                running = False
                terminate = True

        pygame.display.update()
    if terminate:
        pygame.quit()
