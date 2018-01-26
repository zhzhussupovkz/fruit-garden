# -*- coding: utf-8 -*-

#Level - main game logic class
class Level():
    def __init__(self, world):
        self.world = world
        self.num = 1
        self.map = pygame.image.load("./images/levels/level{}.png".format(self.num)).convert()
        self.hero = Hero(self.world)
        self.generator = LevelGenerator(self.num, self.world)
        self.generator.start_point(self.hero)
        self.stars = self.generator.generate_stars()
        self.trees = self.generator.generate_trees()
        self.enemies = self.generator.generate_enemies()

    def draw(self):
        for tree in self.trees:
            tree.draw()
        for star in self.stars:
            star.draw()
        for enemy in self.enemies:
            enemy.draw()
        self.hero.drawing()
