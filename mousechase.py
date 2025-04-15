import pygame
from pygame.locals import*
from time import*

pygame.init()
screen=pygame.display.set_mode((1000,590))
x=500 
y=0
x2=500
y2=0

keys=[False,False,False,False]

bg=pygame.image.load("staircase.jpg")
tom=pygame.image.load("tomcat.png")
jerry=pygame.image.load("jerrymouse.png")

while y<625:
    screen.blit(bg,(0,0))
    screen.blit(tom,(x,y))
    screen.blit(jerry,(x2,y2))
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
    sleep(0.05)
    pygame.display.update()
