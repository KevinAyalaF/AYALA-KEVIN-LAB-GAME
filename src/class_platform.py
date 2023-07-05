import pygame
from settings import *



class Platform:
    def __init__(self, lst: list):
        self.platform = lst
        self.rectangles = self.get_rec()

    def get_rec(self):
        list_rect = []
        for x in range(len(self.platform)):
            list_rect.append(pygame.rect.Rect(self.platform[x]))
        return list_rect
