import pygame
from pygame.locals import*
from time import*

pygame.init()
screen=pygame.display.set_mode((1000,625))
x=500
y=0

keys=[False,False,False,False]

bg=pygame.image.load("pastelgalaxy.jpg")
sauce=pygame.image.load("flyingsaucer.png")

while y<625:
    screen.blit(bg,(0,0))
    screen.blit(sauce,(x,y))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        if event.type==pygame.KEYDOWN:
            if event.key==K_UP:
                keys[0]=True
            if event.key==K_DOWN:
                keys[1]=True
            if event.key==K_LEFT:
                keys[2]=True
            if event.key==K_RIGHT:
                keys[3]=True
        if event.type==pygame.KEYUP:
            if event.key==K_UP:
                keys[0]=False
            if event.key==K_DOWN:
                keys[1]=False
            if event.key==K_LEFT:
                keys[2]=False
            if event.key==K_RIGHT:
                keys[3]=False
    if keys[0]:
        if y>0:
            y-=15
    if keys[1]:
        if y<610:
            y+=15
    if keys[2]:
        if x>0:
            x-=15
    if keys[3]:
        if x<940:
            x+=15
    y+=10
    sleep(0.05)
    pygame.display.update()
