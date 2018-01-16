# -*- coding: utf-8 -*-
import pygame
import sys
import random
from core.hero import *
from core.tree import *
from core.star import *

class World():
    SIZE = (640, 640)

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Fruit garden')
        self.pygame = pygame
        self.screen = pygame.display.set_mode(self.SIZE)
        self.background_image = pygame.image.load("./images/levels/level1.png").convert()
        self.hero = Hero(self.screen, 48, 280)
        self.trees, self.stars = [], []
        self.gen_trees()
        self.gen_stars()

    def gen_trees(self):
        i = 64
        while i <= 632:
            self.trees.append(Tree(self.screen, i, 272))
            i += 75
        j = 320
        while j <= 632:
            self.trees.append(Tree(self.screen, j, 560))
            j += 75
        self.trees.append(Tree(self.screen, 560, 320))
        self.trees.append(Tree(self.screen, 560, 350))
        self.trees.append(Tree(self.screen, 596, 364))
        self.trees.append(Tree(self.screen, 596, 386))

    def gen_stars(self):
        i = 248
        while i <= 550:
            self.stars.append(Star(self.screen, i, 287))
            i += 64
        i = 300
        while i <= 540:
            self.stars.append(Star(self.screen, i, 416))
            i += 48
        j = 320
        while j <= 400:
            self.stars.append(Star(self.screen, 576, j))
            j += 32
        i = 332
        while i <= 630:
            self.stars.append(Star(self.screen, i, 576))
            i += 75

        j = 440
        while j <= 520:
            self.stars.append(Star(self.screen, 273, j))
            j += 75

    def draw(self):
        self.hero.draw()
        for tree in self.trees:
            tree.draw()
        for star in self.stars:
            star.draw()

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
