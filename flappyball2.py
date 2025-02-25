import pgzrun, random
TITLE="Flappy Ball"

WIDTH=800
HEIGHT=800

#Random colour for BALL
red=random.randint(0,255)
green=random.randint(0,255)
blue=random.randint(0,255)

combo=red,green,blue
gravity=2000

#Class for BALL
class ball():
    red=random.randint(0,255)
    green=random.randint(0,255)
    blue=random.randint(0,255)
    combo=red,green,blue

    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.vx=300
        self.up=0
        self.radius=60

    def draw(self):
        red=random.randint(0,255)
        green=random.randint(0,255)
        blue=random.randint(0,255)

        combo=red,green,blue
        p=(self.x,self.y)
        screen.draw.filled_circle(p,self.radius,combo)

b1=ball(90,40)
b2=ball(700,40)

b=[b1,b2]

def draw():
    for i in b:
        i.draw()

def update(dt):
    #pass
    #applying gravity
    #saving current speed
    for i in b:
        uy=i.up
        i.up+=gravity*dt
        i.y+=(uy+i.up)*0.5*dt
        
        #detecting and handling bounce
        if i.y>HEIGHT-i.radius:
            i.y=HEIGHT-i.radius
            i.up=-i.up*0.9
        i.x+=i.vx*dt
        #containing ball 
        if i.x<i.radius or i.x>WIDTH-i.radius:
            i.vx=-i.vx

def on_key_down(key):
    if key==keys.SPACE:
        b1.up=-500
    if key==keys.UP:
        b2.up=-500

pgzrun.go()