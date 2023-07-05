import pygame
from settings import *
from animation_settings import *
from class_attack import Attack


class Enemy_crab(pygame.sprite.Sprite):
    def __init__(self, lista: list, coordenate: tuple, file_attack: str, floor) -> None:
        super().__init__()
        self.animations = lista
        self.rect = self.animations[0].get_rect()
        self.rect.midbottom = coordenate
        self.count = 0
        self.image = None
        self.image_attack = file_attack
        self.floor = floor
        self.playing = True
        
        self.playing = True

    def animate(self):
        tam = len(self.animations)
        if self.count > tam:
            self.count = 0
        self.image = self.animations[int(self.count)]
        self.count += 0.05
    def update(self):
        if self.playing:
            self.animate()

    def attack(self, sprite, sprite_ataque):
        if self.playing:
            attack = Attack(self.image_attack, self.rect.midbottom, self.floor, 5)
            sprite.add(attack)
            sprite_ataque.add(attack)
            
    def resume(self):
        self.playing = True
    
    def stop(self):
        self.playing = False
