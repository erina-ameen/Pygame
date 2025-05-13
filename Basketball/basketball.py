import pygame, random
from pygame.locals import *
import os

pygame.init()
pygame.font.init()
pygame.mixer.init()

screen = pygame.display.set_mode((1000, 775))
x=500
y=20
x2=450
y2=475
score=0
keys=[False, False]
hoop=pygame.image.load("hoop.png")
font1=pygame.font.SysFont("Georgia", 30)
font2=pygame.font.SysFont("Georgia", 70)

def drawing():
    Score=font1.render("Score "+str(score),1, (255, 255, 255))
    screen.blit(Score, (0,0))
    
def display_win():
    win=font2.render("You Win!", 1, (0, 255, 0)) 
    screen.fill("white")
    screen.blit(win,(400,350))
    pygame.display.update()
    pygame.time.delay(5000)

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
    drawing()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    ball1.rect.y+=2
    if ball1.rect.y>755:
        ball1.rect.y=20
        ball1.rect.x=random.randint(0,1000)
        score-=1

    if ball1.rect.colliderect(hoop1):
        ball1.rect.x=random.randint(0,1000)
        ball1.rect.y=20
        score+=1

    #hoop movement
    if event.type==pygame.KEYDOWN:
        if event.key==K_LEFT:
            hoop1.rect.x-=4
        if event.key==K_RIGHT:
            hoop1.rect.x+=4
    
    if score==10:
        display_win()
        running=False

    pygame.display.update()

pygame.quit()
