__author__ = 'moyshi'

import math

import pygame

size = 400, 600
white = 255, 255, 255
red = 255, 0, 0
blue = 0, 128, 255
yellow = 255, 255, 128
green = 0, 230, 0
brown = 128, 64, 64
black = 0, 0, 0
r = 100
N = 75
M = 150
i = True

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("bool pgie")
screen.fill(white)
for i in range(0, N, 1):
    alfa = i / N * 2 * math.pi
    m = -r * math.cos(alfa) + M, -r * math.sin(alfa) + M
    b = r * math.cos(alfa) + M, r * math.sin(alfa) + M
    pygame.draw.line(screen, red, m, b, 1)
pygame.display.flip()
while i:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            i = False
pygame.quit()
