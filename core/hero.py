# -*- coding: utf-8 -*-
import pygame
import math
import datetime
from core.weapon import *

# hero class - player
class HeroSprite(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super(HeroSprite, self).__init__()
        self.screen = screen
        self.left, self.right, self.up, self.down = [], [], [], []
        for i in range(9):
            self.left.append(pygame.image.load("./images/hero/hero-left_{}.png".format(i+1)))
            self.right.append(pygame.image.load("./images/hero/hero-right_{}.png".format(i+1)))
            self.down.append(pygame.image.load("./images/hero/hero-down_{}.png".format(i+1)))
            self.up.append(pygame.image.load("./images/hero/hero-up_{}.png".format(i+1)))
        self.index = 0
        self.image = self.right[self.index]
        self.x, self.y, self.face = x, y, 'right'
        self.rect = pygame.Rect(self.x, self.y, 16, 16)

    def move_left(self):
        self.face = 'left'
        self.index += 1
        if self.index >= len(self.left):
            self.index = 0
        self.image = self.left[self.index]
        if self.x >= 32:
            self.rect = pygame.Rect(self.x - 0.25, self.y, 16, 16)
            self.x -= 0.25

    def move_right(self):
        self.face = 'right'
        self.index += 1
        if self.index >= len(self.right):
            self.index = 0
        self.image = self.right[self.index]
        if self.x <= 620:
            self.rect = pygame.Rect(self.x + 0.25, self.y, 16, 16)
            self.x += 0.25

    def move_down(self):
        self.face = 'down'
        self.index += 1
        if self.index >= len(self.down):
            self.index = 0
        self.image = self.down[self.index]
        if self.y <= 620:
            self.rect = pygame.Rect(self.x, self.y + 0.25, 16, 16)
            self.y += 0.25

    def move_up(self):
        self.face = 'up'
        self.index += 1
        if self.index >= len(self.up):
            self.index = 0
        self.image = self.up[self.index]
        if self.y >= 32:
            self.rect = pygame.Rect(self.x, self.y - 0.25, 16, 16)
            self.y -= 0.25

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_RIGHT]:
            self.move_right()
        elif key[pygame.K_LEFT]:
            self.move_left()
        elif key[pygame.K_UP]:
            self.move_up()
        elif key[pygame.K_DOWN]:
            self.move_down()

class Hero(pygame.sprite.Group):
    def __init__(self, world, x, y, lives):
        self.world = world
        self.screen = self.world.screen
        self.hero_sprite = HeroSprite(self.screen, x, y)
        self.x, self.y = self.hero_sprite.x, self.hero_sprite.y
        self.face, self.centerx, self.centery = 'right', self.hero_sprite.rect.centerx, self.hero_sprite.rect.centery
        self.heart_img = pygame.image.load('./images/hero/heart.png')
        self.star_img = pygame.image.load('./images/hero/star.png')
        self.enemy_img = pygame.image.load("./images/enemies/enemy-down.png")
        self.lives, self.stars, self.enemy_score, self.stamina = lives, 0, 0, 100
        self.weapon = Weapon(self.screen, self)
        self.ui = pygame.font.SysFont("monaco", 15)
        self.ui_score = pygame.font.SysFont("monaco", 24)
        super(Hero, self).__init__(self.hero_sprite)

    def drawing(self):
        if self.lives > 0:
            for i in range(self.lives):
                self.screen.blit(self.heart_img, [620-(i*20), 8])
        self.screen.blit(self.star_img, [540, 6])
        self.screen.blit(self.enemy_img, [500, 6])
        ui_stars_score = self.ui_score.render("{}".format(int(self.stars)), 3, (255, 255, 255))
        ui_enemy_score = self.ui_score.render("{}".format(int(self.enemy_score)), 3, (255, 255, 255))
        self.screen.blit(ui_stars_score, [558, 7])
        self.screen.blit(ui_enemy_score, [520, 7])
        self.weapon.draw()
        cyear = datetime.datetime.now().year
        copyright = self.ui.render("Copyright (c) %s by zhzhussupovkz" % cyear, 3, (255, 255, 255))
        self.screen.blit(copyright, [240, 620])

    def update(self):
        self.face = self.hero_sprite.face
        self.x, self.y = self.hero_sprite.x, self.hero_sprite.y
        self.centerx, self.centery = self.hero_sprite.rect.centerx, self.hero_sprite.rect.centery
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self.attack()
        self.weapon.update()
        self.collect_stars()
        self.add_injury_to_enemies()
        super(Hero, self).update()

    # attack by weapon
    def attack(self):
        self.weapon.drawing = True

    # add injury to enemies
    def add_injury_to_enemies(self):
        if self.weapon.drawing == True:
            for enemy in self.world.level.enemies:
                d = math.sqrt((self.weapon.x - enemy.x)**2 + (self.weapon.y - enemy.y)**2)
                if d <= 4:
                    self.weapon.drawing = False
                    self.world.level.enemies.pop(self.world.level.enemies.index(enemy))
                    self.enemy_score += 1
        else:
            for enemy in self.world.level.enemies:
                d_hero = math.sqrt((self.x - enemy.x)**2 + (self.y - enemy.y)**2)
                if d_hero <= 8:
                    self.add_injury()

    # collect stars
    def collect_stars(self):
        for star in self.world.level.stars:
            d = math.sqrt((self.centerx - star.x)**2 + (self.centery - star.y)**2)
            if d <= 16:
                self.world.level.stars.pop(self.world.level.stars.index(star))
                self.stars += 1

    # add injury when enemies attack hero
    def add_injury(self):
        if self.face == 'left':
            self.x += 8
        elif self.face == 'right':
            self.x -= 8
        elif self.face == 'up':
            self.y += 8
        elif self.face == 'down':
            self.y -= 8
        self.stamina -= 10
        if self.stamina <= 0:
            self.stamina = 0
            self.reboot()

    # reboot hero if die
    def reboot(self):
        if self.lives > 1:
            self.lives -= 1
        else:
            self.lives = 3
        start_x = self.world.level.generator.start_point()[0]
        start_y = self.world.level.generator.start_point()[1]
        self.__init__(self.world, start_x, start_y, self.lives)
