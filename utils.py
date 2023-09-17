import pygame
import os

from components.buttons import Button

clock = pygame.time.Clock()
fps = 60
bottom_panel = 120
screen_width = 1000
screen_height = 400 + bottom_panel

groundLevel = screen_height - bottom_panel - 140

leftTextIndention = 25
rightTextIndention = screen_width / 2

red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
gray = (30, 30, 30)
black = (0, 0, 0)

pygame.font.init()
font = pygame.font.SysFont("Times New Roman", 26)
gametitle_font = pygame.font.SysFont("Times New Roman", 50)
author_font = pygame.font.SysFont("Times New Roman", 20)
button_label_font = pygame.font.SysFont("Times New Roman", 16, pygame.font.Font.bold)
item_count_font = pygame.font.SysFont("Times New Roman", 14)

pygame_icon = pygame.image.load('nyebe_black_cutout.png')
pygame.display.set_icon(pygame_icon)

def init_display():
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Turn Base Rougelike Game")
    return screen

class init_draw():
    def __init__(self, screen):
        self.screen = screen

    def draw_bg(self, img):
        self.screen.blit(img, (0, 0))

    def draw_text(self, text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        self.screen.blit(img, (x, y))

    def draw_main_panel(self, img):
        self.screen.blit(img, (0, screen_height - bottom_panel))

    def draw_panel(self, img, x, y):
        self.screen.blit(img, (x, y))

    def draw_name(self, player, enemy):
        playerText = f"{player['name']} HP: {player['hp']}"
        enemyText = f"{enemy['name']} HP: {enemy['hp']}"

        self.draw_text(playerText, font, white, 25, 30)
        self.draw_text(enemyText, font, white, screen_width - (font.size(enemyText)[0] + 25) , 30)

class Computation():
    def centerX(img):
        return screen_width/2 - img.get_width()/2

    def centerY(additionalCompute=0):
        return screen_height/2 + additionalCompute