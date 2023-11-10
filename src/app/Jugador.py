import pygame
import sys
import math
#Player Class
class Player:
    def __init__(self, bg, sprite):
        #parametros y valores iniciales
        self.COORDENADA_X_INICIAL = 1510
        self.COORDENADA_Y_INICIAL = 1950
        self.VELOCIDAD_INICIAL = 3
        self.COLOR_INICIAL = (250, 120, 60, 0)
        self.size = 50
        self.sprite = pygame.transform.scale(sprite,(self.size, self.size))
        # para que las rotaciones no cambien al sprite como tal (pensá en tocar la tecla izquierda cuatro veces y que el avión termine girando, esto lo evita)
        self.spriteConst = self.sprite
        #limites aproximados del mapa
        self.YlimiteArriba = 20
        self.YlimiteAbajo = 2629
        self.XLimiteIzquierdo = 20
        self.XLimiteDerecho = 4385
        
        self.x = self.COORDENADA_X_INICIAL
        self.y = self.COORDENADA_Y_INICIAL
        self.speed = self.VELOCIDAD_INICIAL
        self.color = self.COLOR_INICIAL
        self.rect = self.sprite.get_rect()
        self.rect.center = (self.sprite.get_width()/2, self.sprite.get_height()/2)
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.s_pressed = False
    
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
                        if self.up_pressed:
                            self.sprite = pygame.transform.rotate(self.spriteConst, 45)
                        elif self.down_pressed:
                            self.sprite = pygame.transform.rotate(self.spriteConst, 135)
                        elif self.right_pressed:
                            #does nothing
                            self.sprite = pygame.transform.rotate(self.spriteConst, -90)
                        else:
                            self.sprite = pygame.transform.rotate(self.spriteConst, 90)

                    if event.key == pygame.K_RIGHT:
                        self.right_pressed = True
                        #Setencia para averiguar si alguna diagonal horizontal derecha deba activarse
                        if self.up_pressed:
                            self.sprite = pygame.transform.rotate(self.spriteConst, -45)
                        elif self.down_pressed:
                            self.sprite = pygame.transform.rotate(self.spriteConst, -135)
                        elif self.left_pressed:
                            #does nothing
                            self.sprite = pygame.transform.rotate(self.spriteConst, 90)
                        else:
                            self.sprite = pygame.transform.rotate(self.spriteConst, -90)

                    if event.key == pygame.K_UP:
                        self.up_pressed = True
                        #Setencia para averiguar si alguna diagonal superior deba activarse
                        if self.left_pressed:
                            self.sprite = pygame.transform.rotate(self.spriteConst, 45)
                        elif self.right_pressed:
                            self.sprite = pygame.transform.rotate(self.spriteConst, -45)
                        elif self.down_pressed:
                            #does nothing
                            self.sprite = pygame.transform.rotate(self.spriteConst, 180)
                        else:
                            self.sprite = pygame.transform.rotate(self.spriteConst, 0)

                    if event.key == pygame.K_DOWN:
                        self.down_pressed = True
                        #Setencia para averiguar si alguna diagonal inferior deba activarse
                        if self.left_pressed:
                            self.sprite = pygame.transform.rotate(self.spriteConst, 135)
                        elif self.right_pressed:
                            self.sprite = pygame.transform.rotate(self.spriteConst, -135)
                        elif self.up_pressed:
                            #does nothing
                            self.sprite = pygame.transform.rotate(self.spriteConst, 0)
                        else:
                            self.sprite = pygame.transform.rotate(self.spriteConst, 180)
                    
                    if event.key == pygame.K_s:
                        self.s_pressed = True
                        
                

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.left_pressed = False
                        #Resetea la direccion del avion diagonal horizontal izquierdos a la tecla que siga presionada 
                        if self.up_pressed:
                            self.sprite = pygame.transform.rotate(self.spriteConst, 0)
                        elif self.down_pressed:
                            self.sprite = pygame.transform.rotate(self.spriteConst, 180)
                        elif self.right_pressed:
                            #does nothing
                            self.sprite = pygame.transform.rotate(self.spriteConst, -90)
                        else:
                            self.sprite = pygame.transform.rotate(self.spriteConst, 90)
                        
                    if event.key == pygame.K_RIGHT:
                        self.right_pressed = False
                        #Resetea la direccion del avion diagonal horizontal derechos a la tecla que siga presionada 
                        if self.up_pressed:
                            self.sprite = pygame.transform.rotate(self.spriteConst, 0)
                        elif self.down_pressed:
                            self.sprite = pygame.transform.rotate(self.spriteConst, 180)
                        elif self.left_pressed:
                            #does nothing
                            self.sprite = pygame.transform.rotate(self.spriteConst, 90)
                        else:
                            self.sprite = pygame.transform.rotate(self.spriteConst, -90)

                    if event.key == pygame.K_UP:
                        self.up_pressed = False
                        #Resetea la direccion del avion diagonal superiores a la tecla que siga presionada 
                        if self.left_pressed:
                            self.sprite = pygame.transform.rotate(self.spriteConst, 90)
                        elif self.right_pressed:
                            self.sprite = pygame.transform.rotate(self.spriteConst, -90)
                        elif self.down_pressed:
                            #does nothing
                            self.sprite = pygame.transform.rotate(self.spriteConst, 180)
                        else:
                            self.sprite = pygame.transform.rotate(self.spriteConst, 0)

                    if event.key == pygame.K_DOWN:
                        self.down_pressed = False
                        #Resetea la direccion del avion diagonal inferiores a la tecla que siga presionada 
                        if self.left_pressed:
                            self.sprite = pygame.transform.rotate(self.spriteConst, 90)
                        elif self.right_pressed:
                            self.sprite = pygame.transform.rotate(self.spriteConst, -90)
                        elif self.up_pressed:
                            #does nothing
                            self.sprite = pygame.transform.rotate(self.spriteConst, 0)
                        else:
                            self.sprite = pygame.transform.rotate(self.spriteConst, 180)

                    if event.key == pygame.K_s:
                        self.s_pressed = False

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
        if self.s_pressed:
            self.speed = self.VELOCIDAD_INICIAL * 2
        else:
            self.speed = self.VELOCIDAD_INICIAL
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
        self.rect = pygame.Rect(int(self.x), int(self.y), self.size, self.size)
    
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
    def getRect(self):
        return self.rect