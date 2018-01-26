# -*- coding: utf-8 -*-

from core.level_generator import *

#Level - main game logic class
class Level():
    def __init__(self, world):
        self.world = world
        self.num = 1
        self.map = self.world.pygame.image.load("./images/levels/level{}.png".format(self.num)).convert()
        self.generator = LevelGenerator(self.num, self.world)
        self.stars = self.generator.generate_stars()
        self.trees = self.generator.generate_trees()
        self.enemies = self.generator.generate_enemies()
        self.hero = Hero(self.world, self.generator.start_point()[0], self.generator.start_point()[1], 3)

    def draw(self):
        self.world.screen.blit(self.map, [0, 0])
        for tree in self.trees:
            tree.draw()
        for star in self.stars:
            star.draw()
        for enemy in self.enemies:
            enemy.draw()
        self.hero.drawing()
        self.hero.draw(self.world.screen)

    def update(self):
        for enemy in self.enemies:
            enemy.walk()
        self.hero.update()
