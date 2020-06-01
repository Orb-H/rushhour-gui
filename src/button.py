import pygame
from pygame.locals import *


class Button:
    def __init__(self, msg, font, size, font_color, x, y, width, height, color,
                 color_ac, on_click):
        self.msg = msg
        self.fn = font
        self.s = size
        self.fc = font_color
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.c = color
        self.ca = color_ac
        self.oc = on_click

        self.change_font(font, size)
        self.change_msg(msg, font_color)

    def change_font(self, font, size):
        font = font if font != None else self.fn
        size = size if size != None else self.s
        self.f = pygame.font.Font(font, size)

    def change_msg(self, msg=None, font_color=None):
        msg = msg if msg != None else self.msg
        font_color = font_color if font_color != None else self.fc

        self.r = self.f.render(msg, 1, font_color)
        self.rect = self.r.get_rect()
        self.rect.center = (self.x + self.w / 2, self.y + self.h / 2)

    def render(self, display):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if self.x <= mouse[0] <= self.x + self.w and self.y <= mouse[
                1] <= self.y + self.h:
            pygame.draw.rect(display, self.ca,
                             (self.x, self.y, self.w, self.h))

            if click[0] == 1:
                self.on_click()
        else:
            pygame.draw.rect(display, self.c, (self.x, self.y, self.w, self.h))

        display.blit(self.r, self.rect)

    def on_click(self):
        self.oc()