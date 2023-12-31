import pygame
import random
#Player Class
class Tormenta:
    def __init__(self, bg, sprite):
        self.VELOCIDAD_INICIAL = 2.5
        
        self.size = 350
        self.sprite = pygame.transform.scale(sprite,(self.size, self.size * .75))
        self.speed = self.VELOCIDAD_INICIAL
        self.rect = self.sprite.get_rect()
        self.velX = 0
        self.velY = 0
        #limites aproximados del mapa
        self.YlimiteArriba = 0
        self.YlimiteAbajo = 2649 - self.sprite.get_height()
        self.XLimiteIzquierdo = 0
        self.XLimiteDerecho = 4405 - self.sprite.get_width()
        #coords iniciales
        self.COORDENADA_X_INICIAL = random.randint(self.XLimiteIzquierdo, self.XLimiteDerecho)
        rand = random.randint(0, 1)
        self.COORDENADA_Y_INICIAL = self.YlimiteArriba
        self.x = self.COORDENADA_X_INICIAL
        self.y = self.COORDENADA_Y_INICIAL
        self.target_x = self.x
        self.target_y = self.y
          
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
        self.target_y = random.randint(self.YlimiteArriba, self.YlimiteAbajo)

    def draw(self, win, coords):
        # variables hechas específicamente para hacer blit según la posición de la tormenta
        xBlit = coords[0] + self.getX()
        yBlit = coords[1] + self.getY()
        # hacemos blit
        win.blit(self.sprite, (xBlit, yBlit))
      
    def update(self):
        # coords de distancia entre objetivo y distancia actual
        dx = self.target_x - self.x
        dy = self.target_y - self.y

        # calculo de distancia
        dist = (dx ** 2 + dy ** 2) ** 0.5

        if dist > 0:
            # calcula el paso segun la distancia
            step = min(self.speed, dist)
            direccion = (dx / dist, dy / dist)

            # se mueve
            self.x += step * direccion[0]
            self.y += step * direccion[1]
           
        else:
            self.moverAPuntoAleatorio()
        self.rect = pygame.Rect(int(self.x), int(self.y), self.size, self.size)
    
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    
    def getRet(self):
        return self.rect