# -*- coding: utf-8 -*-
import pygame
import sys
import random
from core.hero import *
from core.tree import *
from core.star import *
from core.enemy import *

class World():
    SIZE = (640, 640)

    def __init__(self):
        pygame.init()
        self.clock=pygame.time.Clock()
        pygame.display.set_caption('Fruit garden')
        self.pygame = pygame
        self.screen = pygame.display.set_mode(self.SIZE)
        self.background_image = pygame.image.load("./images/levels/level1.png").convert()
        self.trees, self.stars, self.enemies = [], [], []
        self.generate_trees()
        self.generate_stars()
        self.generate_enemies()
        self.hero = Hero(self, 48, 266, 3)

    def generate_trees(self):
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

    def generate_stars(self):
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
        j = 460
        while j <= 560:
            self.stars.append(Star(self.screen, 273, j))
            j += 75

    def generate_enemies(self):
        self.enemies.append(Enemy(self.screen, 220, 280, 'left'))
        self.enemies.append(Enemy(self.screen, 460, 280, 'right'))
        self.enemies.append(Enemy(self.screen, 456, 410, 'left'))
        self.enemies.append(Enemy(self.screen, 500, 570, 'right'))
        self.enemies.append(Enemy(self.screen, 273, 500, 'up'))

    def draw(self):
        for tree in self.trees:
            tree.draw()
        for star in self.stars:
            star.draw()
        for enemy in self.enemies:
            enemy.draw()
        self.hero.drawing()
        self.hero.draw(self.screen)

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
            for enemy in self.enemies:
                enemy.walk()
            self.hero.update()
            pygame.display.flip()
            self.clock.tick(480)
        pygame.quit()
