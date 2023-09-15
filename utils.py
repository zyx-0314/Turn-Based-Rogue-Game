import pygame
import os

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

pygame_icon = pygame.image.load('nyebe_black_cutout.png')
pygame.display.set_icon(pygame_icon)

pygame.mixer.init()

dir = 'assets\sounds'
bow_sound = pygame.mixer.Sound(os.path.join(dir, 'bow.ogg'))
spear_sound = pygame.mixer.Sound(os.path.join(dir, 'spear.ogg'))
sword_sound = pygame.mixer.Sound(os.path.join(dir, 'sword.ogg'))
miss_sound = pygame.mixer.Sound(os.path.join(dir, 'miss.ogg'))
drink_sound = pygame.mixer.Sound(os.path.join(dir, 'drink.ogg'))
boost_sound = pygame.mixer.Sound(os.path.join(dir, 'boost.ogg'))
die_sound = pygame.mixer.Sound(os.path.join(dir, 'die.ogg'))

def init_display():
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Turn Base Rougelike Game")
    return screen

class load_and_transform_image():
    def convert(image_path):
        return pygame.image.load(image_path).convert_alpha()

    def scale(image_path, scale_x=2, scale_y=2):
        img = pygame.image.load(image_path).convert_alpha()
        return pygame.transform.scale(img, (img.get_width() * scale_x, img.get_height() * scale_y))

    def background_img(image_path):
        img = pygame.image.load(image_path).convert_alpha()
        return pygame.transform.scale(img, (screen_width, screen_height - bottom_panel))

    def full_background_img(image_path):
        img = pygame.image.load(image_path).convert_alpha()
        return pygame.transform.scale(img, (screen_width, screen_height))

    def main_panel_img(image_path):
        img = pygame.image.load(image_path).convert_alpha()
        return pygame.transform.scale(img, (screen_width, bottom_panel))

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
        self.draw_text(f"{player['name']} HP: {player['hp']}", font, white, 25, screen_height - bottom_panel + 10)
        self.draw_text(f"{enemy['name']} HP: {enemy['hp']}", font, white, screen_width / 2, screen_height - bottom_panel + 10)