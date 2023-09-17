import pygame
import os

pygame.mixer.init()

dir = 'assets\sounds'

bow_sound = pygame.mixer.Sound(os.path.join(dir, 'bow.ogg'))
spear_sound = pygame.mixer.Sound(os.path.join(dir, 'spear.ogg'))
sword_sound = pygame.mixer.Sound(os.path.join(dir, 'sword.ogg'))
miss_sound = pygame.mixer.Sound(os.path.join(dir, 'miss.ogg'))
drink_sound = pygame.mixer.Sound(os.path.join(dir, 'drink.ogg'))
boost_sound = pygame.mixer.Sound(os.path.join(dir, 'boost.ogg'))
die_sound = pygame.mixer.Sound(os.path.join(dir, 'die.ogg'))