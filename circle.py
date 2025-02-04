import pygame
# Initializing window
pygame.init()
WIDTH=1000
HEIGHT=700
screen=pygame.display.set_mode((WIDTH, HEIGHT))

class cshape():
    def __init__(self, colour, center, radius):
        self.circle_surf=screen
        self.colour=colour
        self.center=center
        self.radius=radius

    def draw(self):
        self.circle=pygame.draw.circle(self.circle_surf,self.colour,self.center,self.radius)

c1=cshape("pink",(200,200),80)
play=True
while play:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            play=False
    c1.draw()

    pygame.display.update()
pygame.quit()