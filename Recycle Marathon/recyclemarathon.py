import pygame, random, time
from pygame.locals import*

pygame.init()
WIDTH=1000
HEIGHT=563

screen=pygame.display.set_mode((WIDTH,HEIGHT))

timer=time.time()
score=0
font1=pygame.font.SysFont("Comic Sans", 20)
scoretxt=font1.render("Score:"+str(score),True,"black")

def background(image):
    bg=pygame.image.load(image)
    bg=pygame.transform.scale(bg,(WIDTH,HEIGHT))
    screen.blit(bg,(0,0))

#class for the bin
class binning(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("bin.png")
        self.image=pygame.transform.scale(self.image,(100,108))
        self.rect=self.image.get_rect()

    def UP_DOWN(self,speed):
        self.rect.move_ip(0,speed)
        if self.rect.top<=0 or self.rect.bottom>=563:
            self.rect.move_ip(0,-speed)

    def LEFT_RIGHT(self, speed): 
        self.rect.move_ip(speed,0)
        if self.rect.left<=0 or self.rect.right>=1000:
            self.rect.move_ip(-speed,0)

#class for recyclable objects
class robjects(pygame.sprite.Sprite):
    def __init__(self,obs):
        super().__init__()
        self.image=pygame.image.load(obs)
        self.image=pygame.transform.scale(self.image,(95,95))
        self.rect=self.image.get_rect()

#class for recyclable objects
class nobjects(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.image.load("plasticbag.png")
        self.image=pygame.transform.scale(self.image,(95,95))
        self.rect=self.image.get_rect()

#list for recyclable objects
recs=["napkin.png","paperbag.png","pencil.png"]
rgroup=pygame.sprite.Group()
ngroup=pygame.sprite.Group()
allgroup=pygame.sprite.Group()

for i in range(35):
    nobj=nobjects()
    nobj.rect.x=random.randint(10,990)
    nobj.rect.y=random.randint(10,553)
    ngroup.add(nobj)
    allgroup.add(nobj)
    
for i in range(35):
    obj=robjects(random.choice(recs))
    obj.rect.x=random.randint(10,990)
    obj.rect.y=random.randint(10,553)
    rgroup.add(obj)
    allgroup.add(obj)

bin=binning()
allgroup.add(bin)

clock=pygame.time.Clock()
run=True
velocity=10

while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type==QUIT:
            run=False 
    timetaken=time.time()-timer

    if timetaken>=60:
        if score>=20:
            youwin=pygame.image.load("youwin.png")
            screen.blit(youwin, (0,0))
        else:
            gameover=pygame.image.load("gameover.png")
            screen.blit(gameover, (0,0))    
    else:
        press_key=pygame.key.get_pressed()

        if press_key[K_LEFT]:
            bin.LEFT_RIGHT(-velocity)
        if press_key[K_RIGHT]:
            bin.LEFT_RIGHT(velocity)
        if press_key[K_UP]:
            bin.UP_DOWN(-velocity)
        if press_key[K_DOWN]:
            bin.UP_DOWN(velocity)
        bin_hit_rec=pygame.sprite.spritecollide(bin,rgroup,True)
        bin_hit_nonrec=pygame.sprite.spritecollide(bin,ngroup,True)
        background("recyclebg.png")
 
        for i in bin_hit_rec:
            score+=1
            scoretxt=font1.render("Score:"+str(score),True,"black")
        for i in bin_hit_nonrec:
            score-=1
            scoretxt=font1.render("Score:"+str(score),True,"black")
        
        screen.blit(scoretxt,(10,10))
        countdown=font1.render("Timer:"+str(60-int(timetaken)),True,"black")
        screen.blit(countdown,(880,10))
        allgroup.draw(screen)
    pygame.display.update()

pygame.quit()
