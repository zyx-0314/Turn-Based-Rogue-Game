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
gray = (50, 50, 50)

def init_display():
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Turn Base Rougelike Game Novel Type")
    return screen

class load_and_transform_image():
    def convert(image_path):
        return pygame.image.load(image_path).convert_alpha()

    def background_img(image_path):
        img = pygame.image.load(image_path).convert_alpha()
        return pygame.transform.scale(img, (screen_width, screen_height - bottom_panel))
    
    def main_panel_img(image_path):
        img = pygame.image.load(image_path).convert_alpha()
        return pygame.transform.scale(img, (screen_width, bottom_panel))

pygame.font.init()
font = pygame.font.SysFont("Times New Roman", 26)

class init_draw():
  def __init__(self, screen):
    self.screen = screen

  def draw_bg(self, background_img):
      self.screen.blit(background_img, (0, 0))

  def draw_text(self, text, font, text_col, x, y):
      img = font.render(text, True, text_col)
      self.screen.blit(img, (x, y))

  def draw_panel(self, main_panel_img, draw_text, player, enemy):
      self.screen.blit(main_panel_img, (0, screen_height - bottom_panel))
      draw_text(f"{player.name} HP: {player.hp}", font, white, 25, screen_height - bottom_panel + 10)
      draw_text(f"{enemy.name} HP: {enemy.hp}", font, white, screen_width / 2, screen_height - bottom_panel + 10)