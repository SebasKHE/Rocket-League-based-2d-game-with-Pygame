import pygame
from pygame.sprite import Sprite
from random import randint
from time import sleep

class Coche():

    def __init__(self, pantalla, settings):
        
        self.pantalla = pantalla
        self.settings = settings


        self.imagen = pygame.image.load("rocket-league.png")
        self.rect = self.imagen.get_rect()
        self.rect_pantalla = self.pantalla.get_rect()

        self.rect.bottom = self.rect_pantalla.bottom
        self.rect.centerx = self.rect_pantalla.centerx

        self.center = float (self.rect.centerx)

        self.mover_izq = False
        self.mover_der = False

    def posicionar (self):

        self.pantalla.blit (self.imagen, self.rect)

    def actualizar_posicion (self, settings):

        if self.mover_izq and self.rect.left > 0:
            self.center -= settings.velocidad_coche
        elif self.mover_der and self.rect.right < self.rect_pantalla.right:
            self.center += settings.velocidad_coche
        
        self.rect.centerx = self.center

class Balon(Sprite):

    def __init__(self, pantalla):
        super().__init__()

        self.imagen = pygame.image.load("balon.png")
        self.rect = self.imagen.get_rect()
        self.pantalla = pantalla
        self.pantalla_rect = self.pantalla.get_rect()
        self.balon_hit = 0
        self.lives = 3
        self.y = float(self.rect.y)
        # Posicionar el balón al inicio en una posición aleatoria horizontal
        self.restaurar()

    def blitme(self):
        self.pantalla.blit(self.imagen, self.rect)
        
    def actualizar(self, settings):
        # Hacer caer el balón
        self.y += settings.velocidad_y
        self.rect.y = self.y

        # Verificar si el balón se sale de la pantalla y restaurarlo
        if self.rect.top > self.pantalla_rect.bottom:
            self.restaurar()
            self.lives -= 1
            sleep(1)

    def restaurar(self):
        # Restablecer la posición Y a la parte superior y X a una posición aleatoria
        self.y = self.pantalla_rect.top + self.rect.height
        self.rect.y = self.y
        self.rect.x = randint(0, self.pantalla_rect.width - self.rect.width)

    def bajar_vidas(self, stats):
        
        if self.lives > 0:
            self.lives -= 1
        else:
            stats.game_active = False
            print("Juego finalizado, haz perdido todas las vidas")
    def sumar_puntos(self):
        self.balon_hit += 1