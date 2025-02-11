import pygame

pygame.init()
WIDTH=600
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))
red=(67,255,54)
green=(34,76,52)
blue=(46,213,55)
red2=(77,34,45)
green2=(44,16,82)
blue2=(26,245,5)

screen.fill(red2)
pygame.display.update()

#Class definition for circle
class circle_shape():
    def __init__(self,colour,pos,radius,thickness):
        self.colour=colour
        self.pos=pos
        self.radius=radius
        self.thickness=thickness
        self.screen=screen
    
    def draw(self):
        pygame.draw.circle(self.screen,self.colour,self.pos,self.radius,self.thickness)

#Object Creation
pygame.draw.circle(screen,red,(90,70),60,5)
pygame.display.update()
obj=circle_shape(green2,(67,80),80,10)
obj2=circle_shape(blue,(67,80),75,15)
obj3=circle_shape(blue2,(67,80),70,20)
play=True
while play:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            play=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            obj.draw()
            obj2.draw()
            obj3.draw()
            pygame.display.update()
pygame.quit()