import pygame
import random
import math
import os

from utils import *
from components.ui import *

class Characters():
    def __init__(self, x, y, damage_text_group, folder, name, max_hp, strength, accuracy, critChance, critDamage, weapon):
        self._name = name
        self._folder = folder
        self._max_hp = max_hp
        self._hp = max_hp
        self._strength = strength
        self._base_strength = strength
        self._accuracy = accuracy
        self._base_accuracy = accuracy
        self._critChance = critChance
        self._base_critChance = critChance
        self._critDamage = critDamage
        self._base_critDamage = critDamage
        self._gold = 0
        self._alive = True
        self._status_effect = []
        self._weapon = weapon

        self._damage_text_group = damage_text_group

        self._animation_list = []
        self._frame_index = 0
        self._action = 0
        self._update_time = pygame.time.get_ticks()

        for actionType in ["idle", "attack", "hurt", "dead"]:
            temp_list = []
            imageCount = len(os.listdir(f"assets/characters/{self._folder}/{actionType}"))
            for j in range(imageCount):
                img = pygame.image.load(f"assets/characters/{self._folder}/{actionType}/{j}.png")
                img = pygame.transform.scale(img, (img.get_width() * 2, img.get_height() * 2))
                temp_list.append(img)
            self._animation_list.append(temp_list)

        self._image = self._animation_list[self._action][self._frame_index]
        self._rect = self._image.get_rect()
        self._rect.center = (x, y)

    def draw(self, screen):
        screen.blit(self._image, self._rect)

    def update(self):
        animation_cooldown = 100
        self._image = self._animation_list[self._action][self._frame_index]
        if pygame.time.get_ticks() - self._update_time > animation_cooldown:
            self._update_time = pygame.time.get_ticks()
            self._frame_index += 1
        if self._frame_index >= len(self._animation_list[self._action]):
            if self._action == 3:
                self._frame_index = len(self._animation_list[self._action]) - 1
            else:
                self.idle()

    def update_action(self, new_action):
        if new_action != self._action:
            self._action = new_action
            self._frame_index = 0
            self._update_time = pygame.time.get_ticks()
        else:
            self._frame_index = 0

    def attack(self, target):
        self.update_action(1)

        sound = ''
        if self._weapon == "bow":
            sound = bow_sound
        elif self._weapon == "spear":
            sound = spear_sound
        elif self._weapon == "sword":
            sound = sword_sound

        if (random.randint(0, 100) < self._accuracy):
            if (random.randint(0, 100) < self._critChance):
                target.hurt(math.ceil(self._strength * self._critDamage), "Crit!")
            else:
                target.hurt(self._strength)
            pygame.mixer.Sound.play(sound)
        else:
            text = 'Miss!'
            self._damage_text_group.add(
                DamageText(self._rect.centerx, self._rect.y, text, red)
            )
            pygame.mixer.Sound.play(miss_sound)

    def idle(self):
        self.update_action(0)

    def hurt(self, damage, text = ''):
        self._hp -= damage
        if self._hp < 0:
            self._hp = 0
            text = 'Overkill!'
        elif self._hp == 0:
            text = 'K.O!'
        else:
            text = f'-{damage} HP'

        self._damage_text_group.add(
            DamageText(self._rect.centerx, self._rect.y, text, red)
        )

        self.update_action(2)
        if self._hp <= 0:
            self._alive = False
            self.dead()

    def dead(self):
        pygame.mixer.Sound.play(die_sound)
        self.update_action(3)

    def checkStat(self, stat):
        if stat == "curr hp" or stat == "hp" or stat == "current hp":
            return self._hp
        elif stat == "max hp":
            return self._max_hp

    def checkStatusEffect(self):
        return self._status_effect

    def checkName(self):
        return self._name

    def checkIfAlive(self):
        return self._alive

class Player(Characters):
    def __init__(self, x, y, damage_text_group, init_dict):
        super().__init__(
            x, y, damage_text_group,
            init_dict['folder'], init_dict['name'],
            init_dict['max_hp'], init_dict['strength'],
            init_dict['accuracy'], init_dict['critChance'],
            init_dict['critDamage'], init_dict['weapon']
        )
        self._bag = init_dict['bag']

    def checkBag(self):
        return self._bag

    def use_potion(self, potion):
        pygame.mixer.Sound.play(drink_sound)
        text = ''
        if potion['effect'] == "heal":
            self.heal(potion['value'])
            text = f'+{potion["value"]} HP'
        elif potion['effect'] == "boost_attack":
            self._strength += potion['value']
            text = f'+{potion["value"]} Strength'
        elif potion['effect'] == "cleanse":
            self._status_effect = []
            text = 'Cleanse!'
        elif potion['effect'] == "boost_accuracy":
            self._accuracy += potion['value']
            text = f'+{potion["value"]} Accuracy'
        elif potion['effect'] == "boost_critChance":
            self._critChance += potion['value']
            text = f'+{potion["value"]} Crit Chance'
        elif potion['effect'] == "boost_critDamage":
            self._critDamage += potion['value']
            text = f'+{potion["value"]} Crit Damage'

        if (potion['effect'] != "heal") & (potion['effect'] != "cleanse"):
            self._status_effect.append(potion)

        for items in self._bag:
            if items['name'] == potion['name']:
                items['quantity'] -= 1
                if items['quantity'] == 0:
                    self._bag.remove(items)
        self._damage_text_group.add(
            DamageText(self._rect.centerx, self._rect.y, text, green)
        )

    def use_focus(self):
        pygame.mixer.Sound.play(boost_sound)
        self._accuracy += 5
        self._strength += 5
        self._status_effect.append({
            "name": "Focus",
            "effect": "boost_accuracy",
            "value": 5,
            "type": "skills",
            "turn": 1
        })
        self._status_effect.append({
            "name": "Focus",
            "effect": "boost_attack",
            "value": 5,
            "type": "skills",
            "turn": 1
        })
        self._damage_text_group.add(
            DamageText(self._rect.centerx, self._rect.y, "Focus! +5 Acc & Str", green)
        )

    def status_ware_off(self):
        counter = 1
        holder = []
        for status in self._status_effect:
            status['turn'] -= 1
            counter += 1

            if status['turn'] <= -1:
                if status['effect'] == "boost_attack":
                    self._strength -= status['value']
                elif status['effect'] == "boost_accuracy":
                    self._accuracy -= status['value']
                elif status['effect'] == "boost_critChance":
                    self._critChance -= status['value']
                elif status['effect'] == "boost_critDamage":
                    self._critDamage -= status['value']

                holder.append(status)

        for status in holder:
            self._status_effect.remove(status)

    def heal(self, heal):
        self._hp += heal
        if self._hp > self._max_hp:
            self._hp = self._max_hp

    def add_cash(self, gold):
        self._gold += gold

    def add_item(self, item):
        for items in self._bag:
            if items['name'] == item['name']:
                items['quantity'] += 1
                return
        self._bag.append(item)

class Enemy (Characters):
    def __init__(self, x, y, damage_text_group, init_dict):
        super().__init__(
            x, y, damage_text_group,
            init_dict['folder'], init_dict['name'],
            init_dict['max_hp'], init_dict['strength'],
            init_dict['accuracy'], init_dict['critChance'],
            init_dict['critDamage'], init_dict['weapon']
        )
        self._drop = init_dict['drop']
        self._gold = init_dict['gold']

    def checkDrop(self):
        return self._drop

    def checkGold(self):
        return self._gold