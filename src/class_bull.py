import pygame
from settings import *
import random


class Bull(pygame.sprite.Sprite):
    def __init__(self, diccionary: dict, floor):
        super().__init__()
        self.animations = diccionary
        self.rect = diccionary["bull_derecha"][0].get_rect()
        self.speed_x = 5
        self.step_counter = 0
        self.con = 0
        self.right = random.choice([True, False])
        self.floor = floor
        self.sound = pygame.mixer.Sound("src/resources/sound/soundbull.mp3")
        self.playing = True


        if self.right:
            self.rect.bottomright = (DISPLAY_LEFT, self.floor.top + 10)
        else:
            self.rect.bottomleft = (DISPLAY_RIGHT, self.floor.top + 10)



    def animate(self, animation):
            animations = self.animations[animation]  #Lista de Animaciones
            tam = len(animations)
            if self.step_counter >= tam:   #Si el contador es mayor al tamaño de la lista se reinicia el contador a 0
                self.step_counter = 0
            self.image = animations[int(self.step_counter)]
            self.step_counter += 0.1


    def update(self):
        if self.playing:
            if self.right:
                self.rect.x += self.speed_x
                what_animation = "bull_derecha"
                if self.rect.left > WIDTH:
                    self.kill()
            else:
                self.rect.x -= self.speed_x
                what_animation = "bull_izquierda"  # Cambiar a "bull_izquierda" si es necesario
                if self.rect.right < 0:
                    self.kill()
            self.animate(what_animation)

    def stop(self):
        self.playing = False
        self.speed_x = 0
        self.sound.stop()

    def resume(self):
        self.playing = True
        self.speed_x = 5