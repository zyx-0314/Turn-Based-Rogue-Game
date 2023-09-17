import pygame
import random

from utils import *

from components.buttons import Button

from scenes.mainMenu import MainMenu

pygame.init()

screen = init_display()
draw = init_draw(screen)

MainMenu()

pygame.quit()

