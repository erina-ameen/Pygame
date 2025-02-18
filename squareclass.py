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
        pygame.draw.rect(self.screen, self.colour, self.pos, (self.size, self.size), self.thickness)

square_size=(50, 50)
obj=square_shape(green2, (90, 70), 90, 10)
obj2=square_shape(blue, (110, 90), 90, 15)
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

pygame.quit()