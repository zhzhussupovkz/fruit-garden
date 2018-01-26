# -*- coding: utf-8 -*-
import pygame
import sys
import random
from core.level import *

class World():
    SIZE = (640, 640)

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Fruit garden')
        self.pygame = pygame
        self.screen = pygame.display.set_mode(self.SIZE)
        self.level = Level(self)

    def draw(self):
        self.level.draw()

    def update(self):
        self.level.update()

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                sys.exit()
            self.draw()
            self.update()
            pygame.display.flip()
            self.clock.tick(240)
        pygame.quit()
