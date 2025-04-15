import pygame
from pygame.locals import*

pygame.font.init()
pygame.mixer.init()
WIDTH=1000
HEIGHT=759
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Ninja Fighters")    #title for the window
white=(255, 255, 255)
black=(0, 0, 0)
purple=(201, 140, 209)
blue=(140, 176, 209)
font1=pygame.font.SysFont("Georgia", 30)
font2=pygame.font.SysFont("Times New Roman", 70)

#Variables
framespersecond=60
velocity=7
bulletspeed=9
maxbullet=5

#Images
bg=pygame.image.load("ninjahouse.jpg")
n1=pygame.image.load("ninja1.png")
n2=pygame.image.load("ninja2.png")

#Border
border=pygame.Rect(500,0,5,759)
nhealth1=10
nhealth2=10

#Class for ninja
class ninja(pygame.sprite.Sprite):
    def __init__(self,image,x,y):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
    def UP(self,speed):
        self.rect.move_ip(0,speed)
        if self.rect.top<=0 or self.rect.bottom>=759:
            self.rect.move_ip(0,-speed)
    
    def LEFT_RIGHT(self,speed,player):
        self.rect.move_ip(speed,0)
        if player==1:
            if self.rect.left<=0 or self.rect.right>=border.left:
                self.rect.move_ip(-speed,0)

def drawing():
    screen.blit(bg,(0,0))
    pygame.draw.rect(screen,black,border)
    heathtxt1=font1.render("Health 1: "+str(nhealth1),1,white)
    heathtxt2=font1.render("Health 2: "+str(nhealth2),1,white)
    screen.blit(heathtxt1, (0,0))
    screen.blit(heathtxt2, (800,0))

#Ninja class object
leftninja=ninja(n1,10,350)
rightninja=ninja(n2,840,350)
ninjagroup=pygame.sprite.Group()
ninjagroup.add(leftninja)
ninjagroup.add(rightninja)

run=True
while run:
    for event in pygame.event.get():
        if event.type==QUIT:
            run=False
    drawing()    
    ninjagroup.draw(screen)
    pygame.display.update()

pygame.quit()
