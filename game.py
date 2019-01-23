__author__ = 'moyshi'

import pygame

list_sprite = pygame.sprite.Group()
all_organs = []
all_organs2 = []
all_organs3 = []
z, b = 11, 11
position_in_height = 10
a = 0
list_color = [(255, 0, 0), (0, 128, 255), (255, 255, 128), (0, 230, 0), (128, 64, 64), (0, 0, 0), (255, 255, 255)]
size = 410, 800
white = list_color[6]
red = list_color[0]
blue = list_color[1]
yellow = list_color[2]
green = list_color[3]
brown = list_color[4]
black = list_color[5]
v = 60
clock = pygame.time.Clock()
i = True
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bull's Eye")


def new_row(y, color=black, width=2, position_first=0, overall_Length=4):
    for x in range(position_first * 70 + 10, overall_Length * 70, 70):
        all_organs.append(color)
        all_organs2.append([x, y, 42, 42])
        all_organs3.append(width)


for i in list_color:
    new_row(750, i, 0, a, a + 1)
    a += 1

while i:
    g = 0
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            i = False
        elif event.type == pygame.MOUSEBUTTONDOWN \
                and event.button == 1:
            x, y = pygame.mouse.get_pos()
            if position_in_height < y < position_in_height + 42:
                if 10 < x < 52:
                    z, b = 11, 11
                elif 80 < x < 122:
                    z, b = 81, 11
                elif 150 < x < 192:
                    z, b = 151, 11
                elif 220 < x < 262:
                    z, b = 221, 11
            if 750 < y < 792:
                if 10 < x < 52:
                    all_organs.append(red)
                    all_organs2.append([z, b, 42, 42])
                    all_organs3.append(0)
                elif 80 < x < 122:
                    all_organs.append(blue)
                    all_organs2.append([z, b, 42, 42])
                    all_organs3.append(0)
                elif 150 < x < 192:
                    all_organs.append(yellow)
                    all_organs2.append([z, b, 42, 42])
                    all_organs3.append(0)
                elif 220 < x < 262:
                    all_organs.append(green)
                    all_organs2.append([z, b, 42, 42])
                    all_organs3.append(0)
                elif 290 < x < 332:
                    all_organs.append(brown)
                    all_organs2.append([z, b, 42, 42])
                    all_organs3.append(0)
                elif 360 < x < 402:
                    all_organs.append(black)
                    all_organs2.append([z, b, 42, 42])
                    all_organs3.append(0)
    new_row(position_in_height)
    for s in all_organs:
        pygame.draw.rect(screen, s, all_organs2[g], all_organs3[g])
        g += 1
    pygame.draw.rect(screen, blue, [z - 3, b - 3, 46, 46], 2)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
