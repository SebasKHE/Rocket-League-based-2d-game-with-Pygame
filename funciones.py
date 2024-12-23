import pygame, sys
from time import sleep

def eventos (coche):

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            tecla_precionada(evento, coche)
        elif evento.type == pygame.KEYUP:
            tecla_suelta(evento, coche)

def actualizar_pantalla(settings, pantalla, coche, balon):

    pantalla.fill(settings.color_fondo)
    coche.posicionar()
    balon.blitme()
    pygame.display.flip()

def tecla_precionada (evento, coche):
    
    if evento.key == pygame.K_LEFT:
        coche.mover_izq = True
    if evento.key == pygame.K_RIGHT:
        coche.mover_der = True
        
def tecla_suelta (evento, coche):
    
    if evento.key == pygame.K_LEFT:
        coche.mover_izq = False
    if evento.key == pygame.K_RIGHT:
        coche.mover_der = False

def colision_coche_balon (settings, pantalla, balon, coche,):
    colision = pygame.sprite.collide_rect(coche, balon)
    if colision:
        balon.kill()
        balon.restaurar()
        balon.sumar_puntos()
        