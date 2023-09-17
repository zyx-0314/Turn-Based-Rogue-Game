import pygame

from utils import *

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