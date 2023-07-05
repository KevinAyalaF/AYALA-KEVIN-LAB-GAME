import pygame
import random
from settings import *


class Enemy_fire(pygame.sprite.Sprite):
    def __init__(self, image: str, direction: str, speed) -> None:
        super().__init__()
        self.image = image
        self.rect = image.get_rect()
        self.x = random.randrange(0, WIDTH)
        self.y = random.randrange(30, HEIGHT - 30)
        self.direction = direction
        self.speed = speed
        self.speed_actual = speed
        self.playing = True
        
        if self.direction == "derecha":
            self.rect.midright = (0, self.y)
        elif self.direction == "izquiera":
            self.rect.midleft = (0, self.y)
        else:
            self.rect.midbottom = (self.x, 0)

    def stop(self):
        self.playing = False
        self.speed = 0

    def resume(self):
        self.playing = True
        self.speed = self.speed_actual



    def update(self):
        if self.playing:
            match self.direction:
                case "derecha":
                    self.rect.x += self.speed
                    if self.rect.left > WIDTH:
                        self.kill()
                case "izquierda":
                    self.rect.x -= self.speed
                    if self.rect.right < 0:
                        self.kill()
                case "arriba":
                    self.rect.y += self.speed
                    if self.rect.top > HEIGHT:
                        self.kill()

