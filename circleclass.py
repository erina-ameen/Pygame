import pygame

pygame.init()
WIDTH=600
HEIGHT=600

screen=pygame.display.set_mode((WIDTH,HEIGHT))
red=(255,67,54)
green=(34,76,52)
blue=(46,55,213)
red2=(77,34,45)
green2=(44,82,16)
blue2=(26,5,245)

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

    def growing(self, grow_size):
        self.radius+=grow_size
        pygame.draw.circle(self.screen,self.colour,self.pos,self.radius,self.thickness)


#Object Creation
pygame.draw.circle(screen,red,(67,80),60,5)
pygame.display.update()
obj=circle_shape(green2,(67,80),80,20)
obj2=circle_shape(blue,(67,80),60,15)
obj3=circle_shape(blue2,(67,80),40,10)
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
        elif event.type==pygame.MOUSEBUTTONUP:
            obj.growing(13)
            obj2.growing(9)
            obj3.growing(2)
        elif event.type==pygame.MOUSEMOTION:
            mouse_pos=pygame.mouse.get_pos()
            obj4=circle_shape(red,mouse_pos,7,7)
            obj4.draw()
            pygame.display.update()
pygame.quit()
