import pygame, random
from pygame.locals import *
from time import sleep

pygame.init()
screen = pygame.display.set_mode((1000, 775))
x=500
y=20
x2=450
y2=475
score=0
keys=[False, False]
hoop=pygame.image.load("hoop.png")

class ball(pygame.sprite.Sprite):
    def __init__(self,x,y):   
        super().__init__()
        self.image=pygame.image.load("basketball.png")
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

class hoop(pygame.sprite.Sprite):
    def __init__(self,x,y):   
        super().__init__()
        self.image=pygame.image.load("hoop.png")
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y 

ball1=ball(x,y)
hoop1=hoop(x2,y2)
comms=pygame.sprite.Group()
comms.add(ball1)
comms.add(hoop1)

running=True
while running:
    screen.fill((0, 0, 0))

    #screen.blit(basketball, (x, y))
    #screen.blit(hoop, (x2, y2))

    comms.draw(screen)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    ball1.rect.y+=3
    if ball1.rect.y>755:
        ball1.rect.y=20
        ball1.rect.x=random.randint(0,1000)

    if ball1.rect.colliderect(hoop1):
        ball1.rect.x=random.randint(0,1000)
        ball1.rect.y=20

    #hoop movement
    if event.type==pygame.KEYDOWN:
        if event.key==K_LEFT:
            hoop1.rect.x-=7
        if event.key==K_RIGHT:
            hoop1.rect.x+=7
            
    pygame.display.update()

pygame.quit()
