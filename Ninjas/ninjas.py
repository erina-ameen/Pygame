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
bullets_r=[]
bullets_l=[]

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

    def UP_DOWN(self,speed):
        self.rect.move_ip(0,speed)
        if self.rect.top<=0 or self.rect.bottom>=759:
            self.rect.move_ip(0,-speed)
    
    def LEFT_RIGHT(self,speed,player):
        self.rect.move_ip(speed,0)
        if player==1:
            if self.rect.left<=0 or self.rect.right>=border.left:
                self.rect.move_ip(-speed,0)

        if player==2:
            if self.rect.right>1000 or self.rect.left<border.right:
                self.rect.move_ip(-speed,0)

def display_win(txt):
    win=font2.render(txt, 1, (0,0,225))
    screen.blit(win, (400,400))
    pygame.display.update()
    pygame.time.delay(5000)

def bullet_create():
    for bullet in bullets_l:
        pygame.draw.rect(screen,"purple",bullet)
        bullet.x+=bulletspeed

    for bullet in bullets_r:
        pygame.draw.rect(screen,"blue",bullet)
        bullet.x-=bulletspeed

def collide():
    global nhealth1, nhealth2
    for bullet in bullets_l:
        if rightninja.rect.colliderect(bullet):
            nhealth2-=1
            bullets_l.remove(bullet)
        elif bullet.x>WIDTH:
            bullets_l.remove(bullet)
    for bullet in bullets_r:
        if leftninja.rect.colliderect(bullet):
            nhealth1-=1
            bullets_r.remove(bullet)
        elif bullet.x<0:
            bullets_r.remove(bullet)

left_bullet_hit=pygame.USEREVENT+1
right_bullet_hit=pygame.USEREVENT+2

def text_draw(text):
    winn=font1.render(text,1,white)
    screen.blit(winn,(500,400))
    pygame.display.update()
    pygame.time.delay(5000)

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
        if event.type==KEYDOWN:
            if event.key==K_LCTRL:
                bullet=pygame.Rect(leftninja.rect.x+leftninja.rect.width,leftninja.rect.y+leftninja.rect.height//2,10,5)
                bullets_l.append(bullet)            
                
            if event.key==K_RCTRL:
                bullet=pygame.Rect(rightninja.rect.x,rightninja.rect.y+rightninja.rect.height//2,10,5)
                bullets_r.append(bullet)

        if event.type==left_bullet_hit:
            nhealth1-=1

        if event.type==right_bullet_hit:
            nhealth2-=1
    
    press_key=pygame.key.get_pressed()

    #right ninja movement
    if press_key[K_LEFT]:
        rightninja.LEFT_RIGHT(-velocity,2)
    if press_key[K_RIGHT]:
        rightninja.LEFT_RIGHT(velocity,2)
    if press_key[K_UP]:
        rightninja.UP_DOWN(-velocity)
    if press_key[K_DOWN]:
        rightninja.UP_DOWN(velocity)

    #left ninja movement
    if press_key[K_a]:
        leftninja.LEFT_RIGHT(-velocity,1)
    if press_key[K_d]:
        leftninja.LEFT_RIGHT(velocity,1)
    if press_key[K_w]:
        leftninja.UP_DOWN(-velocity)
    if press_key[K_s]:
        leftninja.UP_DOWN(velocity)

    drawing()
    ninjagroup.draw(screen)
    bullet_create()
    collide()

    if nhealth1<=0:
        text1="Blue Ninja Wins!"
        display_win(text1)
        run=False

    if nhealth2<=0:
        text2="Purple Ninja Wins!"
        display_win(text2)
        run=False

    pygame.display.update()

pygame.quit()
