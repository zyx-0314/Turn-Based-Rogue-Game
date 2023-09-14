import pygame
import os

pygame.init()

clock = pygame.time.Clock()
fps = 60

bottom_panel = 120
screen_width = 1000
screen_height = 400 + bottom_panel

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Turn Base Rougelike Game Novel Type")

font = pygame.font.SysFont("Times New Roman", 26)

red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
gray = (50, 50, 50)

background_img = pygame.image.load("assets/background/dansel.jpg").convert_alpha()
main_panel_img = pygame.image.load("assets/panels/main panel.png").convert_alpha()

background_img = pygame.transform.scale(background_img, (screen_width, screen_height - bottom_panel))
main_panel_img = pygame.transform.scale(main_panel_img, (screen_width, bottom_panel))

def draw_bg():
    screen.blit(background_img, (0, 0))

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def draw_panel():
    screen.blit(main_panel_img, (0, screen_height - bottom_panel))
    draw_text(f"{mc.name} HP: {mc.hp}", font, white, 25, screen_height - bottom_panel + 10)
    draw_text(f"{skeleton.name} HP: {skeleton.hp}", font, white, screen_width / 2, screen_height - bottom_panel + 10)


class Characters():
    def __init__(self, x, y, name, max_hp, strength, potions):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.start_potions = potions
        self.potions = potions
        self.alive = True

        self.animation_list = []
        self.frame_index = 0
        self.action = 1
        self.update_time = pygame.time.get_ticks()

        for actionType in ["idle", "attack", "hurt", "dead"]:
            temp_list = []
            imageCount = len(os.listdir(f"assets/characters/{self.name}/{actionType}"))
            for j in range(imageCount):
                img = pygame.image.load(f"assets/characters/{self.name}/{actionType}/{j}.png")
                img = pygame.transform.scale(img, (img.get_width() * 2, img.get_height() * 2))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self):
        screen.blit(self.image, self.rect)

    def update(self):
        animation_cooldown = 100
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            self.frame_index = 0
    
class HealthBar():
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def draw(self, hp):
        self.hp = hp
        ratio = self.hp / self.max_hp
        pygame.draw.rect(screen, red, (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, green, (self.x, self.y, 150 * ratio, 20))

class Enemy (Characters):
    def __init__(self, x, y, name, max_hp, strength, potions, drop):
        super().__init__(x, y, name, max_hp, strength, potions)
        self.drop = drop

soil = screen_height - bottom_panel - 140

mc = Characters(200, soil, "mc", 30, 10, 3)
skeleton = Enemy(screen_width-200, soil, "skeleton", 20, 6, 1, 'potion')

mc_health_bar = HealthBar(100, screen_height - bottom_panel - 40, mc.hp, mc.max_hp)
skeleton_health_bar = HealthBar(screen_width - 100, screen_height - bottom_panel - 40, skeleton.hp, skeleton.max_hp)

run = True
while run:
    clock.tick(fps)

    draw_bg()
    draw_panel()

    mc.update()
    mc.draw()
    mc_health_bar.draw(mc.hp)
    skeleton.update()
    skeleton.draw()
    skeleton_health_bar.draw(skeleton.hp)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
