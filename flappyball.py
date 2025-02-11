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
        p=(self.x,self.y)
        screen.draw.filled_circle(p,self.radius,combo)

b1=ball(90,40)
b2=ball(700,40)

def draw():
    screen.clear()
    b1.draw()
    b2.draw()

def update(dt):
    pass
    #applying gravity
    #saving current speed
    uy=b1.up
    b1.up+=gravity*dt
    b1.y+=(uy+b1.up)*0.5*dt
    uy=b2.up
    b2.up+=gravity*dt
    b2.y+=(uy+b1.up)*0.5*dt
    
    #detecting and handling bounce
    if b1.y>HEIGHT-b1.radius:
       b1.y=HEIGHT-b1.radius
       b1.up=-b1.up*0.9
    b1.x+=b1.vx*dt
    if b2.y>HEIGHT-b2.radius:
       b2.y=HEIGHT-b2.radius
       b2.up=-b2.up*0.9
    b2.x+=b2.vx*dt

    #containing ball 
    if b1.x<b1.radius or b1.x>WIDTH-b1.radius:
        b1.vx=-b1.vx
    if b2.x<b2.radius or b2.x>WIDTH-b2.radius:
        b2.vx=-b2.vx

def on_key_down(key):
    if key==keys.SPACE:
        b1.up=-500
    if key==keys.UP:
        b2.up=-500

pgzrun.go()
