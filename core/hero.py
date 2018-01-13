# -*- coding: utf-8 -*-
import pygame
from core.weapon import *

class Hero():
    def __init__(self, screen, x, y):
        self.screen = screen
        self.image = pygame.image.load("./images/hero/player-down.png")
        self.heart = pygame.image.load('./images/hero/heart.png')
        self.x, self.y, self.face, self.lives = x, y, 'down', 3
        self.weapon = Weapon(self.screen, self)

    def draw(self):
        if self.lives > 0:
            for i in range(self.lives):
                self.screen.blit(self.heart, [620-(i*20), 8])
        self.screen.blit(self.image, [self.x, self.y])
        self.weapon.draw()

    def move_left(self):
        self.image = pygame.image.load("./images/hero/player-left.png")
        self.face = 'left'
        if self.x >= 32:
            self.x -= 0.4

    def move_right(self):
        self.image = pygame.image.load("./images/hero/player-right.png")
        self.face = 'right'
        if self.x <= 620:
            self.x += 0.4

    def move_down(self):
        self.image = pygame.image.load("./images/hero/player-down.png")
        self.face = 'down'
        if self.y <= 620:
            self.y += 0.5

    def move_up(self):
        self.image = pygame.image.load("./images/hero/player-up.png")
        self.face = 'up'
        if self.y >= 32:
            self.y -= 0.4

    def walk(self):
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
        # print (self.weapon.x, self.weapon.y)
