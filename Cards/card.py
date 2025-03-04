import pygame, time

pygame.init()  #initialising window
screen=pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Card Slideshow")  #setting title for the screen

bg1=pygame.image.load("birthdaybear.jpg")
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    
    font1=pygame.font.SysFont("Bethany Elingstone",150)
    happy=font1.render("Happy",True,(0,0,0))
    bday=font1.render("Birthday",True,(0,0,0))
    screen.blit(bg1,(0,0))
    screen.blit(happy,(350,650))
    screen.blit(bday,(300,750))
    pygame.display.update()
    time.sleep(3)
    bg2=pygame.image.load("eidmoon.jpg")  #image 2
    bg2=pygame.transform.scale(bg2,(1000,1000))
    font1=pygame.font.SysFont("Dreaming Outloud Pro",150)
    eid=font1.render("Eid",True,(255,255,255))
    mubarak=font1.render("Mubarak",True,(255,255,255))
    screen.blit(bg2,(0,0))
    screen.blit(eid,(320,650))
    screen.blit(mubarak,(300,750))
    pygame.display.update()
    time.sleep(3)