import pygame
from pygame import *
import sys
from pygame.locals import *
class GameOver:
    def __init__(self, tiempo):
        #Path de recursos
        self.ubicacionBG = "recursos/bg/bg_menu.png"        
        
        #Declaraciones Constantes
        self.gris = (156, 156, 156)
        self.blanco = (255, 255, 255)
        self.verde = (70, 189, 34)
        self.naranja = (237, 128, 19)
        self.tiempo = str(tiempo)
        self.WIDTH, self.HEIGHT = 1280, 720
        self.bg_menu = pygame.image.load(self.ubicacionBG)
        self.surface = pygame.display.set_mode((1280, 720))
        self.TITLE = "Geoplane - Game Over"
        #Coordenadas de los elementos
        self.tituloXCoord = 640
        self.tituloYCoord = 265
        self.tiempoXCoord = 640
        self.tiempoYCoord = 320


        self.volver = Rect(300,550, 150, 50)
        #Sintaxis: varName = recta(X, Y, Ancho, Largo)
        
        self.myFont = pygame.font.Font('freesansbold.ttf', 20)
        self.tiempoFont = pygame.font.Font('freesansbold.ttf', 40)
        self.titleFont = pygame.font.Font('freesansbold.ttf', 50)
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

    def mostrarPantalla(self):
        pygame.display.set_caption(self.TITLE)
        self.repetir = True
        self.win.blit(self.bg_menu, (0, 0))
        self.tituloGO = self.titleFont.render("Tiempo final:", True, self.blanco, self.gris)
        self.tiempoGO = self.titleFont.render(self.tiempo + " segundos", True, self.blanco, self.gris)
        self.tituloXCoord -= self.tituloGO.get_width()/2
        self.tiempoXCoord -= self.tiempoGO.get_width()/2
        self.win.blit(self.tituloGO, (self.tituloXCoord, self.tituloYCoord))
        self.win.blit(self.tiempoGO, (self.tiempoXCoord, self.tiempoYCoord))
        while self.repetir:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if self.volver.collidepoint(mouse.get_pos()):
                        self.repetir = False
            self.pintar_boton(self.win, self.volver, "Volver")
            pygame.display.flip()
        pygame.display.set_caption('Geoplane')


    #Constructor de botones
    def pintar_boton(self, win, rect, texto):
        self.buttonRender = self.myFont.render(texto, True, self.blanco)

        #Cuando el mouse se para encima del boton
        if rect.collidepoint(mouse.get_pos()):
            draw.rect(win, self.naranja, rect, 0)
        else:
            draw.rect(win, self.verde, rect, 0)
        win.blit(self.buttonRender, (rect.x + (rect.width - self.buttonRender.get_width())//2, rect.y + (rect.height - self.buttonRender.get_height())//2))