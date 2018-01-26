# -*- coding: utf-8 -*-

from core.hero import *
from core.tree import *
from core.star import *
from core.enemy import *

#LevelGenerator - create game environment for each level
class LevelGenerator():
    def __init__(self, num, world):
        self.num, self.screen = num, world.screen

    def start_point(self):
        if self.num == 1:
            return (48, 266)

    def generate_trees(self):
        trees = []
        if self.num == 1:
            i = 64
            while i <= 632:
                trees.append(Tree(self.screen, i, 272))
                i += 75
            j = 320
            while j <= 632:
                trees.append(Tree(self.screen, j, 560))
                j += 75
            trees.append(Tree(self.screen, 560, 320))
            trees.append(Tree(self.screen, 560, 350))
            trees.append(Tree(self.screen, 596, 364))
            trees.append(Tree(self.screen, 596, 386))
            return trees

    def generate_stars(self):
        stars = []
        if self.num == 1:
            i = 248
            while i <= 550:
                stars.append(Star(self.screen, i, 287))
                i += 64
            i = 300
            while i <= 540:
                stars.append(Star(self.screen, i, 416))
                i += 48
            j = 320
            while j <= 400:
                stars.append(Star(self.screen, 576, j))
                j += 32
            i = 332
            while i <= 630:
                stars.append(Star(self.screen, i, 576))
                i += 75
            j = 460
            while j <= 560:
                stars.append(Star(self.screen, 273, j))
                j += 75
        return stars

    def generate_enemies(self):
        enemies = []
        if self.num == 1:
            enemies.append(Enemy(self.screen, 220, 280, 'left'))
            enemies.append(Enemy(self.screen, 460, 280, 'right'))
            enemies.append(Enemy(self.screen, 456, 410, 'left'))
            enemies.append(Enemy(self.screen, 500, 570, 'right'))
            enemies.append(Enemy(self.screen, 263, 500, 'up'))
        return enemies
