__author__ = 'moyshi'
import pygame

white = 255, 255, 255
red = 255, 0, 0
blue = 0, 128, 255
yellow = 255, 255, 128
green = 0, 230, 0
brown = 128, 64, 64
black = 0, 0, 0


class move(pygame.sprite.Sprite):
    def __init__(self, rec):
        super(move, self).__init__()
        self.pink = 200, 191, 231
        self.image = rec
        self.rect = self.image.get_rect()
        self.rect.x = 23
        self.rect.y = 45
