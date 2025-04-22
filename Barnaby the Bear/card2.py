import pygame, time

pygame.init()  #initialising window
screen=pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Barnaby's Blueberry Muffins")  #setting title for the screen

bg1=pygame.image.load("culinarybear.png")
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    
    font1=pygame.font.SysFont("Bethany Elingstone",70)
    culinarybear=font1.render("Barnaby the bear ",True,(0,0,0))
    culinarybear2=font1.render("loved to bake! ",True,(0,0,0))
    screen.blit(bg1,(0,0))
    screen.blit(culinarybear,(300,700))
    screen.blit(culinarybear2,(330,750))
    pygame.display.update()
    time.sleep(3)

    bg2=pygame.image.load("bearthinkingofblueberrymuffin.png")  #image 2
    bg2=pygame.transform.scale(bg2,(1000,1000))
    bearthinking=font1.render("One sunny morning, ",True,(0,0,0))
    bearthinking2=font1.render("he decided to make ",True,(0,0,0))
    bearthinking3=font1.render("blueberry muffins.",True,(0,0,0))
    screen.blit(bg2,(0,0))
    screen.blit(bearthinking,(270,660))
    screen.blit(bearthinking2,(270,710))
    screen.blit(bearthinking3,(290,760))
    pygame.display.update()
    time.sleep(3)

    bg3=pygame.image.load("bakingbear.png")  #image 3
    bg3=pygame.transform.scale(bg3,(1000,1000))
    bakingbear=font1.render("He carefully mixed ",True,(0,0,0))
    bakingbear2=font1.render("the flour, sugar, and eggs",True,(0,0,0))
    bakingbear3=font1.render("in a big bowl",True,(0,0,0))
    screen.blit(bg3,(0,0))
    screen.blit(bakingbear,(290,660))
    screen.blit(bakingbear2,(230,710))
    screen.blit(bakingbear3,(330,760))
    pygame.display.update()
    time.sleep(3)

    bg4=pygame.image.load("blueberrymuffinbakingbear.png")  #image 4
    bg4=pygame.transform.scale(bg4,(1000,1000))
    blueberrymuffinbakingbear=font1.render("Then, he gently folded in ",True,(0,0,0))
    blueberrymuffinbakingbear2=font1.render("juicy, plump blueberries. ",True,(0,0,0))
    screen.blit(bg4,(0,0))
    screen.blit(blueberrymuffinbakingbear,(200,660))
    screen.blit(blueberrymuffinbakingbear2,(210,710))
    pygame.display.update()
    time.sleep(3)

    bg5=pygame.image.load("smellofmuffins.png")  #image 5
    bg5=pygame.transform.scale(bg5,(1000,1000))
    smell=font1.render("The sweet smell filled his ",True,(0,0,0))
    smell2=font1.render("cozy kitchen as the muffins ",True,(0,0,0))
    smell3=font1.render("baked in the warm oven.",True,(0,0,0))
    screen.blit(bg5,(0,0))
    screen.blit(smell,(200,660))
    screen.blit(smell2,(210,710))
    screen.blit(smell3,(20,760))
    pygame.display.update()
    time.sleep(3)

    bg6=pygame.image.load("blueberrymuffin.png")  #image 6
    bg6=pygame.transform.scale(bg6,(1000,1000))
    muff=font1.render("Soon, golden brown muffins sat ",True,(255,255,255))
    muff2=font1.render("sat cooling on a wire rack. ",True,(255,255,255))
    muff3=font1.render("Barnaby smiled, ready to share his ",True,(255,255,255))
    muff4=font1.render("delicious treat with his friends.",True,(255,255,255))
    screen.blit(bg6,(0,0))
    screen.blit(muff,(150,640))
    screen.blit(muff2,(200,680))
    screen.blit(muff3,(130,720))
    screen.blit(muff4,(180,760))
    pygame.display.update()
    time.sleep(3)