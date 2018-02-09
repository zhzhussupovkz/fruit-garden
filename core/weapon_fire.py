# -*- coding: utf-8 -*-
import pygame

class WeaponFireSprite(pygame.sprite.Sprite):
    def __init__(self, screen, x, y):
        super(WeaponFireSprite, self).__init__()
        self.x, self.y = x, y
        self.screen = screen
        self.images = []
        for i in range(6):
            self.images.append(pygame.image.load("./images/enemies/weapon-fire-right_{}.png".format(i+1)))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(self.x, self.y, 32, 32)

    def update(self):
        self.index += 1
        if self.index >= len(self.images) * 20:
            self.index = 0
        if self.index % 20 == 0:
            self.image = self.images[int(self.index/20)]
        super(WeaponFireSprite, self).update()

# enemy's weapon class (fire)
class WeaponFire(pygame.sprite.Group):
    def __init__(self, screen, enemy):
        self.enemy, self.screen = enemy, screen
        self.x, self.y = self.enemy.x - 6, self.enemy.y + 4
        self.weapon_fire_sprite = WeaponFireSprite(self.screen, self.x, self.y)
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.centerx, self.centery = self.rect.center
        self.drawing, self.last_direction = False, self.enemy.face
        super(WeaponFire, self).__init__(self.weapon_fire_sprite)

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, 16, 16)
        self.centerx, self.centery = self.rect.center
        if self.drawing:
            if self.last_direction == 'left':
                if self.x >= 2:
                    self.x -= 4
            elif self.last_direction == 'right':
                if self.x <= 632:
                    self.x += 4
            elif self.last_direction == 'up':
                if self.y >= 2:
                    self.y -= 4
            elif self.last_direction == 'down':
                if self.y <= 632:
                    self.y += 4
            if self.x <= 4 or self.x >= 632 or self.y <= 4 or self.y >= 632:
                self.drawing = False
                self.last_direction = self.enemy.face
        else:
            self.last_direction = self.enemy.face
            if self.enemy.face == 'left':
                self.x, self.y = self.enemy.x + 12, self.enemy.y + 16
            elif self.enemy.face == 'right':
                self.x, self.y = self.enemy.x + 12, self.enemy.y + 16
            elif self.enemy.face == 'up':
                self.x, self.y = self.enemy.x + 12, self.enemy.y + 16
            elif self.enemy.face == 'down':
                self.x, self.y = self.enemy.x + 12, self.enemy.y + 16

