import pygame
import sys
from pygame.locals import *
from Jugador import Player
from Tormenta import Tormenta

class Game:
    def __init__(self):
        self.ubicacionAvionNegro="recursos/miscellaneous/avioncitoNegro.png"
        self.ubicacionAvionBlanco="recursos/miscellaneous/avioncitoBlanco.png"
        self.ubicacionMapa = "recursos/miscellaneous/mapa.jpg"
        self.ubicacionTormenta = "recursos/miscellaneous/tormenta.png"
    
        #Constantes
        self.WIDTH, self.HEIGHT = 1280, 720
        self.surface = pygame.display.set_mode((1280, 720))
        self.TITLE = "Geoplane"
        self.bg = pygame.image.load(self.ubicacionMapa)
        self.spriteAvion = pygame.image.load(self.ubicacionAvionNegro)
        self.spriteTormenta = pygame.image.load(self.ubicacionTormenta)
        self.player = Player(self.bg, self.spriteAvion)
        self.storm = Tormenta(self.bg, self.spriteTormenta)
        self.clock = pygame.time.Clock()
        self.clock.tick(120)
        #coords
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
        
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
    def empezarPartida(self):
        self.bg = pygame.transform.scale(self.bg, (4405,2649))
        

    #Main Loop
        while True:
            #detectar EventKey
            self.player.detectar_EventKey()
            #Draw
            self.draw()
            #update
            self.update()
            
            
    #Fin def empezarPartida()

    def draw(self):
        self.win.fill((255, 0, 255))
        # coordenadas para mostrar el mapa
        self.mapaCoords = (-self.player.getX() + self.WIDTH/2, -self.player.getY()+ self.HEIGHT/2)
        self.win.blit(self.bg, self.mapaCoords)
        self.player.draw(self.win)
        # la tormenta se dibuja relativa al mapa
        self.storm.draw(self.win, self.mapaCoords)
        self.mostrarCoordsDelAvion()
 
     
    def update(self):
        self.player.update()
        self.storm.update()
        pygame.display.flip()
        
    def mostrarCoordsDelAvion(self):
        #(texto, antialias true o false, colorLetras, colorDeFondo)
        self.text = self.font.render("    X = " + str(self.player.getX()) + "  Y = " + str(self.player.y) + "    ", False, self.colorLetrasCoords, self.colorFondoCoords) 
        self.win.blit(self.text, self.textRect)
    
