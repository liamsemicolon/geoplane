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
        self.player = Player(self.bg)
        self.sprite = pygame.image.load(self.ubicacionAvionNegro)
        self.spriteTormenta = pygame.image.load(self.ubicacionTormenta)
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
        
        #avion y tormentas
        self.TAMAÑO_AVION = 35
        self.TAMAÑO_TORMENTA = 50
        
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
    def empezarPartida(self):
        self.bg = pygame.transform.scale(self.bg, (4405,2649))
        #Player Initialization
        self.sprite = self.avion()
        self.spriteTormenta = self.tormenta()
        

    #Main Loop
        while True:
            #detectar EventKey
            self.detectar_EventKey()
            #Draw
            self.draw()
            #update
            self.update()
            
            
    #Fin def empezarPartida()

    def detectar_EventKey(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.left_pressed = True
                        self.sprite = pygame.transform.rotate(self.avion(), 90)
                    if event.key == pygame.K_RIGHT:
                        self.player.right_pressed = True
                        #sprite = pygame.transform.flip(avion(),True,False)
                        self.sprite = pygame.transform.rotate(self.avion(), -90)
                    if event.key == pygame.K_UP:
                        self.player.up_pressed = True
                        #sprite = pygame.transform.flip(avion(),False,False)
                        self.sprite = pygame.transform.rotate(self.avion(), 0)
                    if event.key == pygame.K_DOWN:
                        self.player.down_pressed = True
                        #sprite = pygame.transform.flip(avion(),False,True)
                        self.sprite = pygame.transform.rotate(self.avion(), 180)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.player.left_pressed = False
                    if event.key == pygame.K_RIGHT:
                        self.player.right_pressed = False
                    if event.key == pygame.K_UP:
                        self.player.up_pressed = False
                    if event.key == pygame.K_DOWN:
                        self.player.down_pressed = False

    def draw(self):
        self.win.fill((12, 24, 36))
        self.win.blit(self.bg, (self.player.x, self.player.y))
        t = Tormenta(self.bg)
        self.win.blit(self.spriteTormenta, (t.getX(), t.getY()))
        self.win.blit(self.sprite, (self.WIDTH/2-self.sprite.get_width()/2, self.HEIGHT/2-self.sprite.get_height()/2))
        
        self.mostrarCordsDelAvion()
 
     
    def update(self):
        self.player.update()
        pygame.display.flip()
        clock = pygame.time.Clock()

        self.clock.tick(120)
        
    def mostrarCordsDelAvion(self):
        #(texto, antialias true o false, colorLetras, colorDeFondo)
        self.text = self.font.render("    X = " + str(self.player.getX()) + "  Y = " + str(self.player.y) + "    ", False, self.colorLetrasCoords, self.colorFondoCoords) 
        self.win.blit(self.text, self.textRect)
        
    def avion(self):
        tamaño=self.TAMAÑO_AVION
        avion = pygame.image.load(self.ubicacionAvionNegro)
        avion = pygame.transform.scale(avion,(tamaño, tamaño))
        return avion
    
    def tormenta(self):
        tamañoTormenta=self.TAMAÑO_TORMENTA
        tormenta= pygame.image.load(self.ubicacionTormenta)
        tormenta = pygame.transform.scale(tormenta,(tamañoTormenta, tamañoTormenta))
        return tormenta