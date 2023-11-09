import pygame
import random
#Player Class
class Tormenta:
    def __init__(self, bg):
        #parametros y valores iniciales
        self.COORDENADA_X_INICIAL = -872
        self.COORDENADA_Y_INICIAL = -1594
        self.VELOCIDAD_INICIAL = 4
        self.COLOR_INICIAL = (250, 120, 60, 0)
        
        #limites aproximados del mapa
        self.YlimiteArriba = 326
        self.YlimiteAbajo = -2254
        self.XLimiteIzquierdo = 610
        self.XLimiteDerecho = -3730
        
        self.x = self.COORDENADA_X_INICIAL
        self.y = self.COORDENADA_Y_INICIAL
        self.speed = self.VELOCIDAD_INICIAL
        self.color = self.COLOR_INICIAL
        self.rect = bg.get_rect()
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.target_x = self.x
        self.target_y = self.y
        
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        
    def colisionBordeArriba(self):
        nuevoY = self.y + self.speed
        if(nuevoY>self.YlimiteArriba):
            return True
    def colisionBordeAbajo(self):
        nuevoY = self.y - self.speed
        if(nuevoY<self.YlimiteAbajo):
            return True
    def colisionBordeIzquierdo(self):
        nuevoX = self.x + self.speed
        if(nuevoX>self.XLimiteIzquierdo):
            return True
    def colisionBordeDerecho(self):
        nuevoX = self.x - self.speed
        if(nuevoX<self.XLimiteDerecho):
            return True
        
    def moverAPuntoAleatorio(self):
        self.target_x = random.randint(self.XLimiteIzquierdo, self.XLimiteDerecho)
        self.target_y = random.randint(self.YlimiteAbajo, self.YlimiteArriba)

    def update(self):
         # Calculate the difference between the current position and the target position
        dx = self.target_x - self.x
        dy = self.target_y - self.y

        # Calculate the distance to the target position
        distance = (dx ** 2 + dy ** 2) ** 0.5

        if distance > 0:
            # Calculate the movement step based on the speed
            step = min(self.move_speed, distance)
            direction = (dx / distance, dy / distance)

            # Update the Tormenta's position
            self.x += step * direction[0]
            self.y += step * direction[1]

        print("tx=" + str(self.x) + "  ty= "+ str(self.y))
        self.rect = pygame.Rect(int(self.x), int(self.y), 128, 128)
    
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def disminuirVelocidad(self, disminuir):
        self.speed -= disminuir
    def aumentarVelocidad(self, aumentar):
        self.speed += aumentar
    def volverLaVelocidadALaOriginal(self):
        self.speed = self.VELOCIDAD_INICIAL