import pygame
#Player Class
class Player:
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
    def update(self):
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            if(self.colisionBordeIzquierdo()!=True):
                self.velX = self.speed
            print("x=" + str(self.x) + "  y= "+ str(self.y))
            
        if self.right_pressed and not self.left_pressed:
            if(self.colisionBordeDerecho()!=True):
                self.velX = -self.speed
            print("x=" + str(self.x) + "  y= "+ str(self.y))
            
        if self.up_pressed and not self.down_pressed:
            if(self.colisionBordeArriba()!=True):
                self.velY = self.speed
            print("x=" + str(self.x) + "  y= "+ str(self.y))
            
        if self.down_pressed and not self.up_pressed:
            if(self.colisionBordeAbajo()!=True):
                self.velY = -self.speed 
            print("x=" + str(self.x) + "  y= "+ str(self.y))
        self.x += self.velX
        self.y += self.velY
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