# -*- coding: utf-8 -*-
import pygame

class Hero():
    def __init__(self, screen, x, y):
        self.image = pygame.image.load("./images/hero/player-down.png")
        self.heart = pygame.image.load('./images/hero/heart.png')
        self.x, self.y = x, y
        self.screen = screen
        self.lives = 3

    def draw(self):
        self.screen.blit(self.image, [self.x, self.y])

    def move_left(self):
        self.image = pygame.image.load("./images/hero/player-left.png")
        if self.x >= 32:
            self.x -= 0.4

    def move_right(self):
        self.image = pygame.image.load("./images/hero/player-right.png")
        if self.x <= 732:
            self.x += 0.4

    def move_down(self):
        self.image = pygame.image.load("./images/hero/player-down.png")
        if self.y <= 550:
            self.y += 0.5

    def move_up(self):
        self.image = pygame.image.load("./images/hero/player-up.png")
        if self.y >= 240:
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
