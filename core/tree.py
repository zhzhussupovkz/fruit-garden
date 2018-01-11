# -*- coding: utf-8 -*-
import pygame

class Tree():
    def __init__(self, screen, x, y):
        self.image = pygame.image.load("./images/resources/tree.png")
        self.image_apple = pygame.image.load("./images/resources/tree-apple.png")
        self.x, self.y = x, y
        self.screen = screen
        self.apple = False

    def draw(self):
        if self.apple:
            self.screen.blit(self.image_apple, [self.x, self.y])
        else:
            self.screen.blit(self.image, [self.x, self.y])
