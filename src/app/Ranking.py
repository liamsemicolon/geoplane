import pygame
from pygame import *
import sys
from pygame.locals import *
from RankingDAO import RankingDAO
class Ranking:
    def __init__(self):
        #Path de recursos
        self.ubicacionBG = "recursos/bg/bg_menu.png"        
        
        #Declaraciones Constantes
        self.gris = (156, 156, 156)
        self.blanco = (255, 255, 255)
        self.verde = (70, 189, 34)
        self.naranja = (237, 128, 19)

        self.valorPuntajeConst = 100
        self.coordYRankingConst = 140
        self.WIDTH, self.HEIGHT = 1280, 720
        self.bg_menu = pygame.image.load(self.ubicacionBG)
        self.surface = pygame.display.set_mode((1280, 720))
        self.TITLE = "Geoplane - Rankings"
        #lista de Rankings
        self.rankings = [
            ("LASH", 10000),
            ("LIAM", 9000),
            ("ARIE", 8000),
            ("ARID", 7000),
            ("AGUS", 6000),
        ]

        #Coordenadas de los elementos
        self.tituloCoord = (330, 90)
        self.coordXRanking = 450
        self.coordYRanking = 140

        self.volver = Rect(300,550, 150, 50)
        #Sintaxis: varName = recta(X, Y, Ancho, Largo)
        
        self.myFont = pygame.font.Font('freesansbold.ttf', 20)
        self.rankingFont = pygame.font.Font('freesansbold.ttf', 40)
        self.titleFont = pygame.font.Font('freesansbold.ttf', 50)
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

    def mostrarRanking(self):
        pygame.display.set_caption(self.TITLE)
        self.repetir = True
        self.win.blit(self.bg_menu, (0, 0))
        self.tituloRank = self.titleFont.render("Leaderboard:", True, self.blanco, self.gris)
        self.win.blit(self.tituloRank, self.tituloCoord)
        self.obtenerDatosRanking()

        while self.repetir:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == MOUSEBUTTONDOWN and event.button == 1:
                    if self.volver.collidepoint(mouse.get_pos()):
                        self.repetir = False
            
            self.drawElementosRanking()
            pygame.display.flip()


    def obtenerDatosRanking(self):
        #Logica de sockets por acá

        self.i = 0
        self.sorter = lambda x:(x[1])
        self.rankings.sort(key=self.sorter, reverse=True)
        for elemento in self.rankings:
            self.i += 1
            self.texto = f"{self.i}. {elemento[0]}............{elemento[1]}"
            self.texto_superficie = self.rankingFont.render(self.texto, True, self.blanco, self.gris)
            self.win.blit(self.texto_superficie, (self.coordXRanking, self.coordYRanking))
            self.coordYRanking += 40  # Ajustar la posición vertical para el siguiente elemento
        self.coordYRanking = self.coordYRankingConst

    def drawElementosRanking(self):
        self.pintar_boton(self.win, self.volver, "Volver")
        

    #Constructor de botones
    def pintar_boton(self, win, rect, texto):
        self.buttonRender = self.myFont.render(texto, True, self.blanco)

        #Cuando el mouse se para encima del boton
        if rect.collidepoint(mouse.get_pos()):
            draw.rect(win, self.naranja, rect, 0)
        else:
            draw.rect(win, self.verde, rect, 0)
        win.blit(self.buttonRender, (rect.x + (rect.width - self.buttonRender.get_width())//2, rect.y + (rect.height - self.buttonRender.get_height())//2))

    def cargarRankingsPickle():
        rankingDao = RankingDAO()
        puntajesDelRanking = rankingDao.unpickleArchivoDePuntajes()
        return puntajesDelRanking
    
    def guardarRankingPickle(listaDePuntajes):
        rankingDao = RankingDAO()
        rankingDao.pickleArchivoDePuntajes( listaDePuntajes)
    
    def añadirPuntaje(self, nombre, tiempo):
        self.jugador = (str(nombre), int(tiempo * self.valorPuntajeConst))
        self.rankings.append(self.jugador)
