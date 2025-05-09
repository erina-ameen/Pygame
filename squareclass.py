import pygame

pygame.init()
WIDTH=600
HEIGHT=600

screen=pygame.display.set_mode((WIDTH, HEIGHT))
red=(188, 37, 95)
green=(78, 90, 5)
blue=(146, 23, 255)
red2=(177, 34, 78)
green2=(44, 216, 182)
blue2=(26, 45, 135)

screen.fill(red2)

class square_shape():
    def __init__(self, colour, pos, size, thickness):
        self.colour=colour
        self.pos=pos
        self.size=size
        self.thickness=thickness
        self.screen=screen

    def draw(self):
        pygame.draw.rect(self.screen, self.colour, (*self.pos, self.size, self.size), self.thickness)

    def growing(self, grow_size):
        self.size+=grow_size
        pygame.draw.rect(self.screen,self.colour,(*self.pos, self.size, self.size),self.thickness)

square_size=(50, 50)
obj=square_shape(green2, (130, 110), 150, 10)
obj2=square_shape(blue, (130, 110), 120, 15)
obj3=square_shape(blue2, (130, 110), 90, 20)

obj.draw()
obj2.draw()
obj3.draw()
pygame.display.update()

play=True
while play:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            play=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            screen.fill(red2)
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
            obj4=square_shape(green2,mouse_pos,7,7)
            obj4.draw()
            pygame.display.update()

pygame.quit()
