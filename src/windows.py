import pygame
from settings import *

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Definir tamaño de la pantalla
width = 640
height = 480

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode(SIZE_SCREEN)
clock = pygame.time.Clock()

# Definir la clase MenuItem
class MenuItem:
    def __init__(self, attributes, font):
        self.font = font
        self.text = attributes['text']
        self.position = attributes['position']
        self.normal_color = attributes['normal_color']
        self.hover_color = attributes['hover_color']
        self.rendered_text = self.font.render(self.text, True, self.normal_color)
        self.rect = self.rendered_text.get_rect()
        self.rect.center = self.position

    def is_hovered(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            if self.is_hovered(mouse_pos):
                self.rendered_text = self.font.render(self.text, True, self.hover_color)
            else:
                self.rendered_text = self.font.render(self.text, True, self.normal_color)

    def draw(self, surface):
        surface.blit(self.rendered_text, self.rect)

# Definir la clase Menu
class Item:
    def __init__(self, items, font):
        self.items = []
        for item in items:
            menu_item = MenuItem(item, font)
            self.items.append(menu_item)

    def handle_event(self, event):
        for item in self.items:
            item.handle_event(event)

    def draw(self, surface):
        for item in self.items:
            item.draw(surface)







