__author__ = 'moyshi'

import pygame

from move2 import move

size = (434, 659)
pink = (200, 191, 231)
b = (255, 255, 255)
mousePos = pygame.sprite.Group()
z = 1
u = 1
v = 60
g = 1
k = 1
dx = 1
dy = 1
y = 200
x = 100
l = r'.\01 מחרוזת פריד (mp3cut).mp3'
m = r'.\Capture.PNG'
a = r'.\mmm.jpg'
def mp3(l):
    pygame.mixer.init()
    pygame.mixer.music.load(l)
    pygame.mixer.music.play()
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('uru')
img = pygame.image.load(a)
screen.blit(img, (0, 0))
n = pygame.image.load(m).convert()
n.set_colorkey(pink)
clock = pygame.time.Clock()
finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        elif event.type == pygame.MOUSEBUTTONDOWN \
                and event.button == 1:
            mousePos.add(move(z, b))
        elif event.type == pygame.MOUSEBUTTONDOWN \
                and event.button == 3:
            mp3(l)
        elif event.type == pygame.MOUSEBUTTONDOWN \
                and event.button == 2:
            k = -k
        elif event.type == pygame.KEYDOWN \
                and event.key == pygame.K_w:
            b -= 10
        elif event.type == pygame.KEYDOWN \
                and event.key == pygame.K_s:
            b += 10
        elif event.type == pygame.KEYDOWN \
                and event.key == pygame.K_a:
            z -= 10
        elif event.type == pygame.KEYDOWN \
                and event.key == pygame.K_d:
            z += 10
        elif event.type == pygame.KEYDOWN \
                and event.key == pygame.K_z:
            mousePos.empty()
        elif event.type == pygame.KEYDOWN \
                and event.key == pygame.K_x:
            g = -g
        elif event.type == pygame.KEYDOWN \
                and event.key == pygame.K_e:
            v -= 10
        elif event.type == pygame.KEYDOWN \
                and event.key == pygame.K_r:
            v += 10
    screen.blit(img, (0, 0))
    # mousePos.add(move(z, b))
    # mousePos[0]
    if k == 1:
        z, b = pygame.mouse.get_pos()
        pygame.mouse.set_visible(False)
    else:
        pygame.mouse.set_visible(True)
    screen.blit(n, (z, b))
    if g == 1:
        for i in mousePos:
            i.mov()
    #    mousePos1 = []
    # for spri in mousePos:
    #   lll = pygame.sprite.spritecollide(spri, mousePos, False)
    #  if len(lll) != 1:
    #     mousePos.remove(spri)
    #  mousePos.empty()
    # for spr in mousePos1:
    #    mousePos.add(spr)
    mousePos.draw(screen)
    pygame.display.flip()
    clock.tick(v)
pygame.quit()
