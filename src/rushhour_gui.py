import pygame
import sys
from pygame.locals import *
from button import Button


def change_screen(num):
    global screen_num
    screen_num = num


width = 800
height = 600
fps = 30

pygame.init()

pygame.display.set_caption("Rush Hour")
display = pygame.display.set_mode((width, height), 0, 32)
clock = pygame.time.Clock()

screen_num = 0  # 0 for title

np_120 = pygame.font.Font("../resources/fonts/NANUMPEN.TTF", 120)

# screen_num 0 (title screen)
title = np_120.render("Rush Hour", 1, (0, 0, 0))
title_rect = title.get_rect()
title_rect.center = (width / 2, height / 2 - 50)

b = Button("Start", "../resources/fonts/NANUMSQUAREROUNDR.TTF", 30, (0, 0, 0),
           300, 450, 200, 50, (191, 191, 191), (255, 255, 255),
           lambda: change_screen(1))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    display.fill((32, 128, 191))

    if screen_num == 0:  # title screen
        display.blit(title, title_rect)
        b.render(display)

    pygame.display.update()
    clock.tick(fps)
