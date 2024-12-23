import pygame
from settings5 import Settings5
import funciones as f
from coche import Coche, Balon
from stats import Stats


def run_game():

    pygame.init()
    settings = Settings5()
    pantalla5 = pygame.display.set_mode((settings.ancho_pantalla, settings.alto_pantalla))
    pygame.display.set_caption("Rocket League chiviado")

    coche = Coche(pantalla5, settings)
    balon = Balon(pantalla5)
    stats = Stats()

    while True:
        f.eventos(coche)
        if stats.game_active:
            coche.actualizar_posicion(settings)
            balon.actualizar(settings)
            f.colision_coche_balon(settings, pantalla5, balon, coche)
        
        f.actualizar_pantalla(settings, pantalla5, coche, balon)
        print("Puntos: " + str(balon.balon_hit))
        print("Vidas restantes: " + str(balon.lives))

run_game()
