# -*- coding: utf-8 -*-
import pygame
import random

# enemy class - enemies
class Enemy():
    def __init__(self, screen, x, y, face):
        self.screen = screen
        self.left = pygame.image.load("./images/enemies/enemy-left.png")
        self.right = pygame.image.load("./images/enemies/enemy-right.png")
        self.up = pygame.image.load("./images/enemies/enemy-up.png")
        self.down = pygame.image.load("./images/enemies/enemy-down.png")
        self.x, self.y, self.face = x, y, face
        self.right_x, self.left_x = self.x + random.randint(64, 72), self.x - random.randint(64, 72)
        self.down_y, self.up_y = self.y + random.randint(64, 72), self.y - random.randint(64, 72)

    def draw(self):
        if self.face == 'left':
            self.screen.blit(self.left, [self.x, self.y])
        elif self.face == 'right':
            self.screen.blit(self.right, [self.x, self.y])
        elif self.face == 'up':
            self.screen.blit(self.up, [self.x, self.y])
        elif self.face == 'down':
            self.screen.blit(self.down, [self.x, self.y])

    def walk(self):
        if self.face == 'right':
            if self.x <= self.right_x:
                self.x += 0.08
            else:
                self.face = 'left'
        elif self.face == 'left':
            if self.x >= self.left_x:
                self.x -= 0.08
            else:
                self.face = 'right'
        elif self.face == 'down':
            if self.y <= self.down_y:
                self.y += 0.08
            else:
                self.face == 'up'
        elif self.face == 'up':
            if self.y >= self.up_y:
                self.y -= 0.08
            else:
                self.face = 'down'
