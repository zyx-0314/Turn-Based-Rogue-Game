import pygame
import random

from utils import *
from components.buttons import Button
from scenes.battle import BattleScene
from components.characters import Player, Enemy
from stats.characterStats import PlayerStat, MonsterStat
from components.imageLoader import load_and_transform_image

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

def setCharacter(SelectedCharacter):
    return Player(200, groundLevel, SelectedCharacter)

def SelectionScene():
    Samurai = setCharacter(PlayerStat.Samurai)

    while True:
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
                            response = 'asd'
                            if character.name == "samurai":
                                response = BattleScene(Samurai, randomizeEnemy())
                            if character.name == "archer":
                                response = BattleScene(setCharacter(PlayerStat.Archer), randomizeEnemy())

                            if response == 'exit':
                                return False
            if event.type == pygame.QUIT:
                return False

        pygame.display.update()
