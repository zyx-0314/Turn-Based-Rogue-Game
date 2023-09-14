import pygame
import random
import math
import os

from utils import *
from components.ui import *

class Characters():
    def __init__(self, x, y, damage_text_group, folder, name, max_hp, strength, accuracy, critChance, critDamage):
        self.name = name
        self.folder = folder
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.base_strength = strength
        self.accuracy = accuracy
        self.base_accuracy = accuracy
        self.critChance = critChance
        self.base_critChance = critChance
        self.critDamage = critDamage
        self.base_critDamage = critDamage
        self.alive = True
        self.status_effect = []

        self.damage_text_group = damage_text_group

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
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
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
        text = 'Miss!'
        if (random.randint(0, 100) < self.accuracy):
            if (random.randint(0, 100) < self.critChance):
                target.hp -= math.ceil(self.strength * self.critDamage)
                text = f'Crit! {math.ceil(self.strength * self.critDamage)}'
            else:
                target.hp -= self.strength
                text = f'{self.strength}'
            if target.hp < 0:
                target.hp = 0
            target.hurt()
        self.damage_text_group.add(
            DamageText(target.rect.centerx, target.rect.y, text, red)
        )

    def idle(self):
        self.update_action(0)

    def hurt(self):
        self.update_action(2)
        if self.hp <= 0:
            self.alive = False
            self.dead()

    def dead(self):
        self.update_action(3)

class Player(Characters):
    def __init__(self, x, y, damage_text_group, init_dict):
        super().__init__(
            x, y, damage_text_group,
            init_dict['folder'], init_dict['name'],
            init_dict['max_hp'], init_dict['strength'],
            init_dict['accuracy'], init_dict['critChance'],
            init_dict['critDamage']
        )
        self.bag = init_dict['bag']

    def use_potion(self, potion):
        text = ''
        if potion['effect'] == "heal":
            self.heal(potion['value'])
            text = f'+{potion["value"]} HP'
        elif potion['effect'] == "boost_attack":
            self.strength += potion['value']
            text = f'+{potion["value"]} Strength'
        elif potion['effect'] == "cleanse":
            self.status_effect = []
            text = 'Cleanse!'
        elif potion['effect'] == "boost_accuracy":
            self.accuracy += potion['value']
            text = f'+{potion["value"]} Accuracy'
        elif potion['effect'] == "boost_critChance":
            self.critChance += potion['value']
            text = f'+{potion["value"]} Crit Chance'
        elif potion['effect'] == "boost_critDamage":
            self.critDamage += potion['value']
            text = f'+{potion["value"]} Crit Damage'

        if (potion['effect'] != "heal") & (potion['effect'] != "cleanse"):
            self.status_effect.append(potion)

        for items in self.bag:
            if items['name'] == potion['name']:
                items['quantity'] -= 1
                if items['quantity'] == 0:
                    self.bag.remove(items)
        self.damage_text_group.add(
            DamageText(self.rect.centerx, self.rect.y, text, green)
        )

    def use_focus(self):
        self.accuracy += 5
        self.strength += 5
        self.status_effect.append({
            "name": "Focus",
            "effect": "boost_accuracy",
            "value": 5,
            "type": "skills",
            "turn": 1
        })
        self.status_effect.append({
            "name": "Focus",
            "effect": "boost_attack",
            "value": 5,
            "type": "skills",
            "turn": 1
        })
        self.damage_text_group.add(
            DamageText(self.rect.centerx, self.rect.y, "Focus! +5 Acc & Str", green)
        )

    def status_ware_off(self):
        counter = 1
        holder = []
        for status in self.status_effect:
            status['turn'] -= 1
            counter += 1

            if status['turn'] <= -1:
                if status['effect'] == "boost_attack":
                    self.strength -= status['value']
                elif status['effect'] == "boost_accuracy":
                    self.accuracy -= status['value']
                elif status['effect'] == "boost_critChance":
                    self.critChance -= status['value']
                elif status['effect'] == "boost_critDamage":
                    self.critDamage -= status['value']

                holder.append(status)

        for status in holder:
            self.status_effect.remove(status)

    def heal(self, heal):
        self.hp += heal
        if self.hp > self.max_hp:
            self.hp = self.max_hp

class Enemy (Characters):
    def __init__(self, x, y, damage_text_group, init_dict):
        super().__init__(
            x, y, damage_text_group,
            init_dict['folder'], init_dict['name'],
            init_dict['max_hp'], init_dict['strength'],
            init_dict['accuracy'], init_dict['critChance'],
            init_dict['critDamage']
        )
        self.drop = init_dict['drop']
        self.gold = init_dict['gold']