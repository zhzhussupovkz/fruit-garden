# -*- coding: utf-8 -*-

from core.level_generator import *

#Level - main game logic class
class Level():
    def __init__(self, world):
        self.world = world
        self.num = 1
        self.ui = pygame.font.SysFont("monaco", 24)
        self.world.pygame.mouse.set_pos(320, 320)
        self.map = self.world.pygame.image.load("./images/levels/level{}.png".format(self.num)).convert()
        self.scoreboard = self.world.pygame.image.load("./images/levels/scoreboard.png").convert()
        self.generator = LevelGenerator(self.num, self.world)
        self.stars = self.generator.generate_stars()
        self.trees = self.generator.generate_trees()
        self.enemies = self.generator.generate_enemies()
        self.hero = Hero(self.world, self.generator.start_point()[0], self.generator.start_point()[1], 3)

    def draw(self):
        self.world.screen.blit(self.map, [0, 0])
        self.world.screen.blit(self.scoreboard, [0, 0])
        ui_level = self.ui.render("LEVEL {}".format(int(self.num)), 3, (255, 255, 255))
        self.world.screen.blit(ui_level, [280, 5])
        for tree in self.trees:
            tree.draw()
        for star in self.stars:
            star.draw()
        for enemy in self.enemies:
            enemy.draw(self.world.screen)
        self.hero.drawing()
        self.hero.draw(self.world.screen)

    def update(self):
        for enemy in self.enemies:
            enemy.update()
        self.hero.update()
