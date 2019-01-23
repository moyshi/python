__author__ = 'moyshi'
import numpy
import pygame


class move(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(move, self).__init__()
        self.pink = (200, 191, 231)
        self.m = r'.\Capture.PNG'
        self.image = pygame.image.load(self.m).convert()
        self.image.set_colorkey(self.pink)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.dx = 1
        self.dy = 1

    def mov(self):
        if self.rect.x <= 0 or self.rect.x >= 380:
            self.dx *= -1
            self.dx += numpy.sign(self.dx) * 1
            self.dy += numpy.sign(self.dy) * 1
        if self.dx != 1 and self.dx != -1:
            self.dx += -1 * numpy.sign(self.dx)
            self.dy += -1 * numpy.sign(self.dy)
        if self.rect.y <= 0 or self.rect.y >= 609:
            self.dy *= -1
            self.dx += numpy.sign(self.dx) * 1
            self.dy += numpy.sign(self.dy) * 1
        self.rect.y += self.dy
        self.rect.x += self.dx
