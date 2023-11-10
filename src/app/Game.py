import pygame
import sys
from pygame.locals import *
from Jugador import Player
from Tormenta import Tormenta
from GameOver import GameOver

class Game:
    def __init__(self, ranking):
        self.ranking = ranking
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
        self.tormentas = list()
        self.clock = pygame.time.Clock()
        self.clock.tick(120)
        #booleano, será verdadero si hay una colisión
        self.colision = False
        #coords
        self.X_displayCoords = 0
        self.POSICION_X_MOSTRAR_COORDENADAS = 50
        self.POSICION_Y_MOSTRAR_COORDENADAS = 50
        self.POSICION_Y_MOSTRAR_TIME = 100
        self.POSICION_X_MOSTRAR_TIME = 100
        self.BLANCO = (255, 255, 255)
        self.VERDE = (0, 255, 0)
        self.AZUL = (0, 0, 128)
        self.colorLetrasCoords = self.VERDE
        self.colorFondoCoords = self.AZUL
        
        self.fontTime = pygame.font.Font('freesansbold.ttf', 50)
        self.textTime = self.fontTime.render('', True, self.AZUL, None)
        self.textRectTime = self.textTime.get_rect()
        self.textRectTime.center = ( self.POSICION_X_MOSTRAR_TIME // 2, self.POSICION_Y_MOSTRAR_TIME // 2)
        self.tiempoActual = 0
        self.auxiliar = 0
        self.contadorTiempo=0
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

    def empezarPartida(self):
        self.bg = pygame.transform.scale(self.bg, (4405,2649))
        self.colision = False
        self.player = Player(self.bg, self.spriteAvion)
        self.ticks = pygame.time.get_ticks()
        self.contadorTiempo = 0
        self.auxiliar = 0
        self.tormentas = list()
        for i in range (0, 100):
            self.tormentas.append(Tormenta(self.bg, self.spriteTormenta))
    #Main Loop
        while self.colision == False:
            #detectar EventKey
            self.player.detectar_EventKey()
            #Draw
            self.draw()
            #update
            self.update()
        gameOver = GameOver(self.contadorTiempo, self.ranking)
        gameOver.mostrarPantalla()
        self.ranking.mostrarRanking()
    
            
            
    #Fin def empezarPartida()

    def draw(self):
        self.win.fill((0, 86, 164))
        # coordenadas para mostrar el mapa
        self.mapaCoords = (-self.player.getX() + self.WIDTH/2, -self.player.getY()+ self.HEIGHT/2)
        self.win.blit(self.bg, self.mapaCoords)
        self.player.draw(self.win)
        # la tormenta se dibuja relativa al mapa
        for t in self.tormentas:
            t.draw(self.win, self.mapaCoords)
        self.mostrarTime(self.ticks)
 
     
    def update(self):
        self.player.update()
        for t in self.tormentas:
            t.update()
        self.hayColision()     
        pygame.display.flip()
        

    def mostrarTime(self, ticks):
        self.tiempoActual = pygame.time.get_ticks() - ticks
        if self.tiempoActual > self.auxiliar:
            self.auxiliar += 1000
            self.contadorTiempo+=1
        self.textTime = self.fontTime.render(str(self.contadorTiempo) + " s.", True, self.BLANCO, self.AZUL) 
        self.win.blit(self.textTime, self.textRectTime)           
    
    def hayColision(self):
        for t in self.tormentas:
            self.colisionConTormenta(t)
    
    def colisionConTormenta(self, storm):
        if  storm.getRet().contains(self.player.getRect()):
            print("Colision con tormenta")
            self.colision = True