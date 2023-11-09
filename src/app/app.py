import pygame, sys
import pygame_menu
from pygame_menu.examples import create_example_window
from pygame.locals import *
from Game import Game
from Ranking import Ranking

#Constantes
WIDTH, HEIGHT = 1280, 720
TITLE = "Geoplane"
surface = pygame.display.set_mode((1280, 720))
#pygame initialization
COLOR_BLANCO = (255, 255, 255)
COLOR_NEGRO = (255, 255, 255)
FRAME = pygame.display.set_mode((1280, 720))
ubicacionIconoCargar = "recursos/miscellaneous/Icono.png"   

def main_menu():
    pygame.init()
    pygame.display.set_caption('Geoplane')
    icono = pygame.image.load(ubicacionIconoCargar)
    pygame.display.set_icon(icono)
#set color blanco de fondo
    FRAME.fill(COLOR_BLANCO)

#bucle para que no se cierre la ventana
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()          
            menu = pygame_menu.Menu(
            height=720,
            theme=pygame_menu.themes.THEME_BLUE,
            title=TITLE,
            width=1280
        )
        game = Game() #Objeto de tipo Game.py
        ranking = Ranking() #Objeto de tipo Ranking.py
        menu.add.button('Jugar', game.empezarPartida)                
        menu.add.button('Rankings',ranking.mostrarRanking)
        menu.add.button('Salir', pygame_menu.events.EXIT)  
        menu.mainloop(surface)
        pygame.display.update()

main_menu()