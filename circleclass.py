import pygame, random

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

    def shrinking(self, shrink_size):
        self.radius-=shrink_size
        pygame.draw.circle(self.screen,self.colour,self.pos,self.radius,self.thickness)

    def colour_find(self):
        self.colour=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.draw()

    def if_click(self,mouse_pos):
        x=mouse_pos[0]-self.pos[0]
        y=mouse_pos[1]-self.pos[1]
        return x**2+y**2<=self.radius**2

#Object Creation
pygame.draw.circle(screen,red,(67,80),60,5)
pygame.display.update()
obj=circle_shape(green2,(300,300),80,20)
obj2=circle_shape(blue,(300,300),60,15)
obj3=circle_shape(blue2,(300,300),40,10)
objects=[obj,obj2,obj3]
play=True
while play:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            play=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            current=pygame.mouse.get_pos()
            for i in objects:
                if i.if_click(current):
                    i.colour_find()
            pygame.display.update()
            obj.draw()
            obj2.draw()
            obj3.draw()
            pygame.display.update()
        elif event.type==pygame.MOUSEBUTTONUP:
            obj.growing(13)
            obj2.growing(9)
            obj3.growing(2)
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_s:
                obj.shrinking(13)
                obj2.shrinking(9)
                obj3.shrinking(2)
                pygame.display.update()
            if event.key==pygame.K_r:
                obj.shrinking(13)
                obj2.shrinking(9)
                obj3.shrinking(2)
                pygame.display.update()
            
        elif event.type==pygame.MOUSEMOTION:
            mouse_pos=pygame.mouse.get_pos()
            obj4=circle_shape(red,mouse_pos,7,7)
            obj4.draw()
            pygame.display.update()
pygame.quit()
