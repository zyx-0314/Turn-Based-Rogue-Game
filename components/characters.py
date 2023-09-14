import pygame
import random
import os

from utils import *

class Characters():
    def __init__(self, x, y, folder, name, max_hp, strength, accuracy):
        self.name = name
        self.folder = folder
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.base_strength = strength
        self.accuracy = accuracy
        self.alive = True
        self.status_effect = []

        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        for actionType in ["idle", "attack", "hurt", "dead"]:
            temp_list = []
            imageCount = len(os.listdir(f"assets/characters/{self.folder}/{actionType}"))
            for j in range(imageCount):
                img = pygame.image.load(f"assets/characters/{self.folder}/{actionType}/{j}.png")
                img = pygame.transform.scale(img, (img.get_width() * 2, img.get_height() * 2))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        animation_cooldown = 100
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            if self.alive == False:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.update_time = pygame.time.get_ticks()
                self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            self.idle()

    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
        else:
            self.frame_index = 0

    def attack(self, target):
        self.update_action(1)
        if (random.randint(0, 100) < self.accuracy):
            target.hp -= self.strength
            target.hurt()

    def idle(self):
        self.update_action(0)

    def hurt(self):
        self.update_action(2)
        if self.hp <= 0:
            self.alive = False
            self.dead()

    def dead(self):
        self.update_action(3)

class HealthBar():
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def draw(self, screen, hp,):
        self.hp = hp
        ratio = self.hp / self.max_hp
        pygame.draw.rect(screen, red, (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, green, (self.x, self.y, 150 * ratio, 20))

class Player(Characters):
    def __init__(self, x, y, init_dict):
        super().__init__(x, y, init_dict['folder'], init_dict['name'], init_dict['max_hp'], init_dict['strength'], init_dict['accuracy'])
        self.bag = init_dict['bag']

    def use_potion(self, potion):
        if potion['effect'] == "heal":
            self.heal(potion['value'])
        elif potion['effect'] == "boost_attack":
            self.strength += potion['value']
            print(self.strength)
            self.status_effect.append(potion)
        elif potion['effect'] == "cleance":
            self.status_effect = []

        for items in self.bag:
            if items['name'] == potion['name']:
                items['quantity'] -= 1
                if items['quantity'] == 0:
                    self.bag.remove(items)

    def status_ware_off(self):
        for potion in self.status_effect:
            potion['turn'] -= 1
            if potion['turn'] == -1:
                self.strength = self.base_strength
                self.status_effect.remove(potion)

    def heal(self, heal):
        self.hp += heal
        if self.hp > self.max_hp:
            self.hp = self.max_hp

class Enemy (Characters):
    def __init__(self, x, y, init_dict):
        super().__init__(x, y, init_dict['folder'], init_dict['name'], init_dict['max_hp'], init_dict['strength'], init_dict['accuracy'])
        self.drop = init_dict['drop']
