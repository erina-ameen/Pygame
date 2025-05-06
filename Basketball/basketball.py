import pygame
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
basketball=pygame.image.load("basketball.png")
hoop=pygame.image.load("hoop.png")

running=True
while running:
    screen.fill((0, 0, 0))

    screen.blit(basketball, (x, y))
    screen.blit(hoop, (x2, y2))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==K_LEFT:
                keys[0]=True
            if event.key==K_RIGHT:
                keys[1]=True
        if event.type==pygame.KEYUP:
            if event.key==K_LEFT:
                keys[0]=False
            if event.key==K_RIGHT:
                keys[1]=False

    if keys[0]:
        if x2>0:
            x2-=5
    if keys[1]:
        if x2<940:
            x2+=5


    y+=10
    sleep(0.03)
    pygame.display.update()

pygame.quit()