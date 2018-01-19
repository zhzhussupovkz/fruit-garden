# -*- coding: utf-8 -*-
import pygame
from core.weapon import *

# hero class - player
class Hero(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super(Hero, self).__init__()
        self.screen = screen
        self.left, self.right, self.up, self.down = [], [], [], []
        for i in range(9):
            self.left.append(pygame.image.load("./images/hero/hero-left_{}.png".format(i+1)))
            self.right.append(pygame.image.load("./images/hero/hero-right_{}.png".format(i+1)))
            self.down.append(pygame.image.load("./images/hero/hero-down_{}.png".format(i+1)))
            self.up.append(pygame.image.load("./images/hero/hero-up_{}.png".format(i+1)))
        self.index = 0
        self.image = self.left[self.index]
        self.heart = pygame.image.load('./images/hero/heart.png')
        self.x, self.y, self.face, self.lives = x, y, 'down', 3
        self.rect = pygame.Rect(self.x, self.y, 16, 16)
        self.weapon = Weapon(self.screen, self)

    # def drawing(self):
    #     if self.lives > 0:
    #         for i in range(self.lives):
    #             self.screen.blit(self.heart, [620-(i*20), 8])
    #     # self.screen.blit(self.image, [self.x, self.y])
    #     self.weapon.draw()

    def move_left(self):
        self.index += 1
        if self.index >= len(self.left):
            self.index = 0
        self.image = self.left[self.index]
        self.face = 'left'
        if self.x >= 32:
            self.rect = pygame.Rect(self.x - 0.25, self.y, 16, 16)
            self.x -= 0.25

    def move_right(self):
        self.index += 1
        if self.index >= len(self.right):
            self.index = 0
        self.image = self.right[self.index]
        self.face = 'right'
        if self.x <= 620:
            self.rect = pygame.Rect(self.x + 0.25, self.y, 16, 16)
            self.x += 0.25

    def move_down(self):
        self.index += 1
        if self.index >= len(self.down):
            self.index = 0
        self.image = self.down[self.index]
        self.face = 'down'
        if self.y <= 620:
            self.rect = pygame.Rect(self.x, self.y + 0.25, 16, 16)
            self.y += 0.25

    def move_up(self):
        self.index += 1
        if self.index >= len(self.up):
            self.index = 0
        self.image = self.up[self.index]
        self.face = 'up'
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
        self.weapon.update()
