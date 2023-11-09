import pygame

class Coords:
    def __init__(self) -> None:
        self.X_displayCoords = 0
        self.POSICION_X_MOSTRAR_COORDENADAS = 50
        self.POSICION_Y_MOSTRAR_COORDENADAS = 50
        self.BLANCO = (255, 255, 255)
        self.VERDE = (0, 255, 0)
        self.AZUL = (0, 0, 128)
        self.colorLetrasCoords = self.VERDE
        self.colorFondoCoords = self.AZUL
        self.font = pygame.font.Font('freesansbold.ttf', 12)
        self.text = self.font.render('', True, self.VERDE, self.AZUL)
        self.textRect = self.text.get_rect()
        self.textRect.center = ( self.POSICION_X_MOSTRAR_COORDENADAS // 2, self.POSICION_Y_MOSTRAR_COORDENADAS // 2)