# -*- coding: utf-8 -*-
import pygame
import math
from core.weapon import *

# hero class - player
class HeroSprite(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super(HeroSprite, self).__init__()
        self.screen = screen
        self.left, self.right, self.up, self.down = [], [], [], []
        for i in range(9):
            self.left.append(pygame.image.load("./images/hero/hero-left_{}.png".format(i+1)))
            self.right.append(pygame.image.load("./images/hero/hero-right_{}.png".format(i+1)))
            self.down.append(pygame.image.load("./images/hero/hero-down_{}.png".format(i+1)))
            self.up.append(pygame.image.load("./images/hero/hero-up_{}.png".format(i+1)))
        self.index = 0
        self.image = self.right[self.index]
        self.x, self.y, self.face = x, y, 'right'
        self.rect = pygame.Rect(self.x, self.y, 16, 16)

    def move_left(self):
        self.face = 'left'
        self.index += 1
        if self.index >= len(self.left):
            self.index = 0
        self.image = self.left[self.index]
        if self.x >= 32:
            self.rect = pygame.Rect(self.x - 0.25, self.y, 16, 16)
            self.x -= 0.25

    def move_right(self):
        self.face = 'right'
        self.index += 1
        if self.index >= len(self.right):
            self.index = 0
        self.image = self.right[self.index]
        if self.x <= 620:
            self.rect = pygame.Rect(self.x + 0.25, self.y, 16, 16)
            self.x += 0.25

    def move_down(self):
        self.face = 'down'
        self.index += 1
        if self.index >= len(self.down):
            self.index = 0
        self.image = self.down[self.index]
        if self.y <= 620:
            self.rect = pygame.Rect(self.x, self.y + 0.25, 16, 16)
            self.y += 0.25

    def move_up(self):
        self.face = 'up'
        self.index += 1
        if self.index >= len(self.up):
            self.index = 0
        self.image = self.up[self.index]
        if self.y >= 32:
            self.rect = pygame.Rect(self.x, self.y - 0.25, 16, 16)
            self.y -= 0.25

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.move_right()
        elif key[pygame.K_LEFT]:
            self.move_left()
        elif key[pygame.K_UP]:
            self.move_up()
        elif key[pygame.K_DOWN]:
            self.move_down()

class Hero(pygame.sprite.Group):
    def __init__(self, window, screen, x, y):
        self.window, self.screen = window, screen
        self.hero_sprite = HeroSprite(screen, x, y)
        self.x, self.y = self.hero_sprite.x, self.hero_sprite.y
        self.face = 'right'
        self.heart = pygame.image.load('./images/hero/heart.png')
        self.lives = 3
        self.weapon = Weapon(self.screen, self)
        super(Hero, self).__init__(self.hero_sprite)

    def drawing(self):
        if self.lives > 0:
            for i in range(self.lives):
                self.screen.blit(self.heart, [620-(i*20), 8])
        self.weapon.draw()

    def update(self):
        self.face = self.hero_sprite.face
        self.x, self.y = self.hero_sprite.x, self.hero_sprite.y
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.attack()
        self.weapon.update()
        self.add_injury_to_enemies()
        super(Hero, self).update()

    def attack(self):
        self.weapon.drawing = True

    def add_injury_to_enemies(self):
        if self.weapon.drawing == True:
            for enemy in self.window.enemies:
                d = math.sqrt((self.weapon.x - enemy.x)**2 + (self.weapon.y - enemy.y)**2)
                if d <= 4:
                    self.weapon.drawing = False
                    self.window.enemies.pop(self.window.enemies.index(enemy))





