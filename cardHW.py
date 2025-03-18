import pygame, time

pygame.init()  #initialising window
screen=pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Card Slideshow")  #setting title for the screen

font1=pygame.font.SysFont("Times New Roman",100)
font2=pygame.font.SysFont("Georgia",100)
bg1=pygame.image.load("birthdaybear.jpg")
bg2=pygame.image.load("eidmoon.jpeg")  #image 2
bg2=pygame.transform.scale(bg2,(1000,1000))
bg3=pygame.image.load("clouds.jpg") 
happy=font1.render("Happy",True,(0,0,0))
bday=font1.render("Birthday",True,(0,0,0))
eid=font2.render("Eid",True,(255,255,255))
mubarak=font2.render("Mubarak",True,(255,255,255))
current=1

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            current=2 if current==1 else 1
    if current==1:
        screen.blit(bg1,(0,0))
        screen.blit(happy,(350,650))
        screen.blit(bday,(300,750))
    else:
        screen.blit(bg2,(0,0))
        screen.blit(eid,(400,650))
        screen.blit(mubarak,(300,750))
    
    pygame.display.update()
    