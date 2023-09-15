import pygame
import random

from utils import *

from components.buttons import Button

from scenes.battle import BattleScene
from scenes.selection import SelectionScene

pygame.init()

screen = init_display()
draw = init_draw(screen)

background_img = load_and_transform_image.full_background_img("assets/background/dansel.jpg")
main_panel_img = load_and_transform_image.scale("assets/panels/main panel.png", 1, 1.5)
title_panel_img = load_and_transform_image.scale("assets/panels/title.png", 2.8, 2.8)

def centerX(img):
    return screen_width/2 - img.get_width()/2
centerY = screen_height/2

buttonArray = []

counter = -1
for buttonValue in ['exit', 'play']:
    img = load_and_transform_image.scale(f"assets/icons/{buttonValue}.png")
    button = Button(screen, screen_width/2-(img.get_width()/2)-(90*counter), centerY, img, img.get_width(), img.get_height(), buttonValue)
    buttonArray.append(button)
    counter += 2

def MainMenu():
    running = True
    while running:
        clock.tick(fps)

        draw.draw_bg(background_img)
        draw.draw_panel(main_panel_img,centerX(main_panel_img), centerY-23)
        draw.draw_panel(title_panel_img,centerX(title_panel_img), -55)

        draw.draw_text("Turn Based Roguelike Game", gametitle_font, black, screen_width/2 - 260, 50)
        draw.draw_text("by Ian Cedric Ramirez", author_font, gray, screen_width/2 - 100, 100)

        for button in buttonArray:
            button.draw()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button in buttonArray:
                        if button.rect.collidepoint(event.pos):
                            if button.name == "play":
                                SelectionScene()
                            if button.name == "exit":
                                running = False
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
    pygame.quit()

MainMenu()
