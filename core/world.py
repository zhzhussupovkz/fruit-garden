# -*- coding: utf-8 -*-
import pygame
import sys
import random
from core.hero import *
from core.tree import *

class World():
    SIZE = (640, 640)

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Fruit garden')
        self.pygame = pygame
        self.screen = pygame.display.set_mode(self.SIZE)
        self.background_image = pygame.image.load("./images/levels/level1.png").convert()
        self.hero = Hero(self.screen, 48, 280)
        self.trees = []
        self.gen_trees()

    def gen_trees(self):
        i = 64
        while i <= 632:
            self.trees.append(Tree(self.screen, i, 272))
            i += 75

    def draw(self):
        self.hero.draw()
        for tree in self.trees:
            tree.draw()

    def play(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            key = pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                sys.exit()
            self.screen.blit(self.background_image, [0, 0])
            self.draw()
            self.hero.walk()
            pygame.display.flip()
        pygame.quit()
