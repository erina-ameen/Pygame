import pygame
#initialising window
pygame.init()

WIDTH=1000
HEIGHT=700

screen=pygame.display.set_mode((WIDTH,HEIGHT))

class recshapes():
    def __init__(self,colour,dimension):
        self.rec_surf=screen
        self.colour=colour
        self.dimension=dimension
    def draw(self):
        self.rectangle=pygame.draw.rect(self.rec_surf,self.colour,self.dimension)
rec1=recshapes("pink",(200,200,250,280))
rec2=recshapes("pink",(500,200,250,280))
play=True
while play:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            play=False
    rec1.draw()
    rec2.draw()
    pygame.display.update()
pygame.quit()
