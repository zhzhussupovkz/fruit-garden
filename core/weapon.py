# -*- coding: utf-8 -*-
import pygame

class Weapon():
    def __init__(self, screen, hero):
        self.hero = hero
        self.image = pygame.image.load("./images/hero/apple-player.png")
        self.x, self.y = self.hero.x - 6, self.hero.y + 4
        self.screen = screen
        self.drawing, self.last_direction = False, self.hero.face

    def draw(self):
        if self.drawing:
            self.screen.blit(self.image, [self.x, self.y])

    def update(self):
        if self.drawing:
            self.last_direction = self.hero.face
            if self.last_direction == 'left':
                if self.x >= 2:
                    self.x = self.hero.x - 3
                    self.y = self.hero.y + 3
            elif self.last_direction == 'right':
                if self.x <= 632:
                    self.x = self.hero.x + 10
                    self.y = self.hero.y + 4
            elif self.last_direction == 'up':
                if self.y >= 2:
                    self.x = self.hero.x + 4
                    self.y = self.hero.y - 5
            elif self.last_direction == 'down':
                if self.y <= 632:
                    self.x = self.hero.x + 4
                    self.y = self.hero.y + 5
            if self.x <= 4 or self.x >= 632 or self.y <= 4 or self.y >= 632:
                self.drawing = False
                self.last_direction = self.hero.face

