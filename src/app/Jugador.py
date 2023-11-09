import pygame
import sys
#Player Class
class Player:
    def __init__(self, bg, sprite):
        #parametros y valores iniciales
        self.COORDENADA_X_INICIAL = 1510
        self.COORDENADA_Y_INICIAL = 1950
        self.VELOCIDAD_INICIAL = 4
        self.COLOR_INICIAL = (250, 120, 60, 0)
        self.size = 35
        self.sprite = pygame.transform.scale(sprite,(self.size, self.size))
        # para que las rotaciones no cambien al sprite como tal (pensá en tocar la tecla izquierda cuatro veces y que el avión termine girando, esto lo evita)
        self.spriteConst = self.sprite
        #limites aproximados del mapa
        self.YlimiteArriba = 0
        self.YlimiteAbajo = 2649
        self.XLimiteIzquierdo = 0
        self.XLimiteDerecho = 4405
        
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
        win.blit(self.sprite, (1280/2-self.sprite.get_width()/2, 720/2-self.sprite.get_height()/2))


    def detectar_EventKey(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.left_pressed = True
                        self.sprite = pygame.transform.rotate(self.spriteConst, 90)
                    if event.key == pygame.K_RIGHT:
                        self.right_pressed = True
                        #sprite = pygame.transform.flip(avion(),True,False)
                        self.sprite = pygame.transform.rotate(self.spriteConst, -90)
                    if event.key == pygame.K_UP:
                        self.up_pressed = True
                        #sprite = pygame.transform.flip(avion(),False,False)
                        if self.left_pressed == False and self.right_pressed == False:
                            self.sprite = pygame.transform.rotate(self.spriteConst, 0)
                    if event.key == pygame.K_DOWN:
                        self.down_pressed = True
                        #sprite = pygame.transform.flip(avion(),False,True)
                        if self.left_pressed == False and self.right_pressed == False:
                            self.sprite = pygame.transform.rotate(self.spriteConst, 180)
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.left_pressed = False
                    if event.key == pygame.K_RIGHT:
                        self.right_pressed = False
                    if event.key == pygame.K_UP:
                        self.up_pressed = False
                    if event.key == pygame.K_DOWN:
                        self.down_pressed = False

    def colisionBordeArriba(self):
        nuevoY = self.y + self.speed
        if(nuevoY<self.YlimiteArriba):
            return True
    def colisionBordeAbajo(self):
        nuevoY = self.y - self.speed
        if(nuevoY>self.YlimiteAbajo):
            return True
    def colisionBordeIzquierdo(self):
        nuevoX = self.x + self.speed
        if(nuevoX<self.XLimiteIzquierdo):
            return True
    def colisionBordeDerecho(self):
        nuevoX = self.x - self.speed
        if(nuevoX>self.XLimiteDerecho):
            return True
    def update(self):
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            if(self.colisionBordeIzquierdo()!=True):
                self.velX = -self.speed
            
        if self.right_pressed and not self.left_pressed:
            if(self.colisionBordeDerecho()!=True):
                self.velX = self.speed
            
        if self.up_pressed and not self.down_pressed:
            if(self.colisionBordeArriba()!=True):
                self.velY = -self.speed
            
        if self.down_pressed and not self.up_pressed:
            if(self.colisionBordeAbajo()!=True):
                self.velY = self.speed 
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