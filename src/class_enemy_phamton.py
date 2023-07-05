import pygame
from settings import *
from animation_settings import *
import random


class Enemy_phantom(pygame.sprite.Sprite):
    def __init__(self, dic: dict, cordenate: tuple, limit_right: int, limit_left: int) -> None:
        super().__init__()
        self.animations = dic
        self.rect = self.animations["camina_derecha"][0].get_rect()
        self.rect.midbottom = cordenate
        self.right =  random.choice([True, False])
        self.speed_x = 2
        self.step_counter = 0
        self.image = None
        self.limit_right = limit_right
        self.limit_left = limit_left
        self.playing = True

    def update(self):
        if self.playing:
            if self.right:
                what_animation = "camina_derecha"
                self.rect.x += self.speed_x
                if self.rect.right > self.limit_right:  # Si choca con el límite derecho de la pantalla
                    self.right = False  # Cambia la dirección a la izquierda
            else:
                what_animation = "camina_izquierda"
                self.rect.x -= self.speed_x
                if self.rect.left < self.limit_left:  # Si choca con el límite izquierdo de la pantalla
                    self.right = True  # Cambia la dirección a la derecha
            self.animate(what_animation)

    def animate(self, animation):
        animations = self.animations[animation]  #Lista de Animaciones
        tam = len(animations)
        if self.step_counter >= tam:   #Si el contador es mayor al tamaño de la lista se reinicia el contador a 0
            self.step_counter = 0
        self.image = animations[int(self.step_counter)]
        self.step_counter += 0.1

    def stop(self):
        self.playing = False
        self.speed_x = 0

    def resume(self):
        self.playing = True
        self.speed_x = 2

