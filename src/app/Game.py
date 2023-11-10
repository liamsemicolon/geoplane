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
        self.stormDos = Tormenta(self.bg, self.spriteTormenta)
        self.stormTres = Tormenta(self.bg, self.spriteTormenta)
        self.stormCuatro = Tormenta(self.bg, self.spriteTormenta)
        self.stormCinco = Tormenta(self.bg, self.spriteTormenta)
        self.stormSeis = Tormenta(self.bg, self.spriteTormenta)
        self.stormSiete = Tormenta(self.bg, self.spriteTormenta)
        self.stormOcho = Tormenta(self.bg, self.spriteTormenta)
        self.stormNueve = Tormenta(self.bg, self.spriteTormenta)
        self.stormDiez = Tormenta(self.bg, self.spriteTormenta)
        self.tormentas =  [self.storm, self.stormDos,self.stormTres, self.stormCuatro, self.stormCinco, self.stormSeis, self.stormSiete, self.stormOcho, self.stormNueve, self.stormDiez]
        self.clock = pygame.time.Clock()
        self.clock.tick(120)
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
        
        self.fontCoords = pygame.font.Font('freesansbold.ttf', 12)
        self.textCoords = self.fontCoords.render('', True, self.VERDE, self.AZUL)
        self.textRect = self.textCoords.get_rect()
        self.textRect.center = ( self.POSICION_X_MOSTRAR_COORDENADAS // 2, self.POSICION_Y_MOSTRAR_COORDENADAS // 2)
        
        self.fontTime = pygame.font.Font('freesansbold.ttf', 12)
        self.textTime = self.fontTime.render('', True, self.VERDE, self.AZUL)
        self.textRectTime = self.textTime.get_rect()
        self.textRectTime.center = ( self.POSICION_X_MOSTRAR_TIME // 2, self.POSICION_Y_MOSTRAR_TIME // 2)
        self.tiempoActual = 0
        self.auxiliar = 0
        self.contadorTiempo=0
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
        for t in self.tormentas:
            t.draw(self.win, self.mapaCoords)
        self.mostrarCoordsDelAvion()
        self.mostrarTime()
 
     
    def update(self):
        self.player.update()
        for t in self.tormentas:
            t.update()
        self.hayColision()
                
    
    
          
               
        pygame.display.flip()
        
    def mostrarCoordsDelAvion(self):
        #(texto, antialias true o false, colorLetras, colorDeFondo)
        self.textCoords = self.fontCoords.render("    X = " + str(self.player.getX()) + "  Y = " + str(self.player.y) + "    ", False, self.colorLetrasCoords, self.colorFondoCoords) 
        self.win.blit(self.textCoords, self.textRect)
    
    def mostrarTime(self):
        self.tiempoActual = pygame.time.get_ticks()
        if self.tiempoActual > self.auxiliar:
            self.auxiliar += 1000
            self.contadorTiempo+=1
        self.textTime = self.fontTime.render("Tiempo: " + str(self.contadorTiempo), False, self.colorLetrasCoords, self.colorFondoCoords) 
        self.win.blit(self.textTime, self.textRectTime)           
    
    def hayColision(self):
        if self.colisionConTormentaUno():
            return True
        if self.colisionConTormentaDos():
            return True
        if self.colisionConTormentaTres():
            return True
        if self.colisionConTormentaCuatro():
            return True
        if self.colisionConTormentaCinco():
            return True
        if self.colisionConTormentaSeis():
            return True
        if self.colisionConTormentaSiete():
            return True
        if self.colisionConTormentaOcho():
            return True
        if self.colisionConTormentaNueve():
            return True
        if self.colisionConTormentaDiez():
            return True
        return False
    
    def colisionConTormentaUno(self):
        if self.storm.getRet().contains(self.player.getRect()):
            print("Colision con tormenta uno")
            return True
        else:
            return False
    def colisionConTormentaDos(self):
        if self.stormDos.getRet().contains(self.player.getRect()):
            print("Colision con tormenta dos")
            return True
        else:
            return False
    def colisionConTormentaTres(self):
        if self.stormTres.getRet().contains(self.player.getRect()):
            print("Colision con tormenta tres")
            return True
        else:
            return False
    def colisionConTormentaCuatro(self):
        if self.stormCuatro.getRet().contains(self.player.getRect()):
            print("Colision con tormenta cuatro")
            return True
        else:
            return False
    def colisionConTormentaCinco(self):
        if self.stormCinco.getRet().contains(self.player.getRect()):
            print("Colision con tormenta cinco")
            return True
        else:
            return False
    def colisionConTormentaSeis(self):
        if self.stormSeis.getRet().contains(self.player.getRect()):
            print("Colision con tormenta Seis")
            return True
        else:
            return False
    def colisionConTormentaSiete(self):
        if self.stormSiete.getRet().contains(self.player.getRect()):
            print("Colision con tormenta siete")
            return True
        else:
            return False
    def colisionConTormentaOcho(self):
        if self.stormOcho.getRet().contains(self.player.getRect()):
            print("Colision con tormenta ocho")
            return True
        else:
            return False
    def colisionConTormentaNueve(self):
        if self.stormNueve.getRet().contains(self.player.getRect()):
            print("Colision con tormenta nueve")
            return True
        else:
            return False
    def colisionConTormentaDiez(self):
        if self.stormDiez.getRet().contains(self.player.getRect()):
            print("Colision con tormenta diez")
            return True
        else:
            return False