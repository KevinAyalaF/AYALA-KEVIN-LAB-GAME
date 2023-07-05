import pygame

class Cronometro:
    def __init__(self, minutos, segundos=0):
        self.minutos = minutos
        self.segundos = segundos
        self.total_segundos = (self.minutos * 60) + self.segundos
        self.start_time = 0
        self.pause_time = 0
        self.is_finished = False
        self.is_running = False

    def start(self):
        if not self.is_running:
            if self.is_finished:
                self.reset()
            self.start_time = pygame.time.get_ticks()
            self.is_running = True

    def pause(self):
        if self.is_running:
            self.pause_time = pygame.time.get_ticks()
            self.is_running = False

    def resume(self):
        if not self.is_running:
            elapsed_pause_time = pygame.time.get_ticks() - self.pause_time
            self.start_time += elapsed_pause_time
            self.is_running = True

    def stop(self):
        if self.is_running:
            elapsed_time = pygame.time.get_ticks() - self.start_time
            remaining_time = max(0, self.total_segundos - elapsed_time // 1000)
            self.minutos = remaining_time // 60
            self.segundos = remaining_time % 60
            self.is_running = False

    def reset(self, minutos, segundo: int = 0):
        self.minutos = minutos
        self.segundos = segundo
        self.is_finished = False
        self.is_running = False

    def update(self):
        if self.is_running:
            elapsed_time = pygame.time.get_ticks() - self.start_time
            remaining_time = max(0, self.total_segundos - elapsed_time // 1000)
            self.minutos = remaining_time // 60
            self.segundos = remaining_time % 60

            if self.minutos == 0 and self.segundos == 0:
                self.is_finished = True

    def get_time_text(self):
        return f"{self.minutos:02d}:{self.segundos:02d}"

    def draw(self, surface, font, position: tuple, color):
        text = font.render(self.get_time_text(), True, color)
        rect_text = text.get_rect()
        rect_text.midtop = position
        surface.blit(text, rect_text)

