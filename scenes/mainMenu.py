import pygame

from utils import *
from components.imageLoader import *
from components.buttons import Button
from scenes.selection import SelectionScene

screen = init_display()
draw = init_draw(screen)

full_background_img = load_and_transform_image.full_background_img("assets/background/dansel.jpg")
mainmenu_selection_panel_img = load_and_transform_image.scale("assets/panels/main panel.png", 1, 1.5)
title_panel_img = load_and_transform_image.scale("assets/panels/title.png", 2.8, 2.8)

def MainMenu():
    def setButton():
        buttonArray = []
        for index, buttonValue in enumerate(['exit', 'play']):
            img = load_and_transform_image.scale(f"assets/icons/{buttonValue}.png")
            button = Button(screen, (screen_width/2-img.get_width()/2+90)-180*(index), Computation.centerY(), img, img.get_width(), img.get_height(), buttonValue)
            buttonArray.append(button)

        return buttonArray

    while True:
        clock.tick(fps)

        draw.draw_bg(full_background_img)
        draw.draw_panel(mainmenu_selection_panel_img, Computation.centerX(mainmenu_selection_panel_img), Computation.centerY(-23))
        draw.draw_panel(title_panel_img, Computation.centerX(title_panel_img), -55)

        draw.draw_text("Turn Based Rogue Game", gametitle_font, black, screen_width/2 - 260, 50)
        draw.draw_text("by Ian Cedric Ramirez", author_font, gray, screen_width/2 - 100, 100)

        for button in setButton():
            button.draw()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for button in setButton():
                        if button.rect.collidepoint(event.pos):
                            if button.name == "play":
                                 return SelectionScene()
                            if button.name == "exit":
                                return 'exit'
            if event.type == pygame.QUIT:
                return 'exit'

        pygame.display.update()