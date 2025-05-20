import pygame, random, time
from pygame.locals import*

pygame.init()
WIDTH=1000
HEIGHT=563

screen=pygame.display.set_mode((WIDTH,HEIGHT))

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

for i in range(50):
    obj=robjects(random.choice(recs))
    obj.rect.x=random.randint(10,990)
    obj.rect.y=random.randint(10,553)
    rgroup.add(obj)
    allgroup.add(obj)

for i in range(50):
    nobj=nobjects()
    nobj.rect.x=random.randint(10,990)
    nobj.rect.y=random.randint(10,553)
    ngroup.add(nobj)
    allgroup.add(nobj)

bin=binning()
allgroup.add(bin)

clock=pygame.time.Clock()
run=True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type==QUIT:
            run-False

    background("recyclebg.png")
    allgroup.draw(screen)
    pygame.display.update()

pygame.quit()
