import pygame, random
from pygame.locals import*

pygame.font.init()
pygame.mixer.init()
WIDTH=1000
HEIGHT=563
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Project")    #title for the window
bg=pygame.image.load("vortex.jpg")
paddle=pygame.image.load("paddle.png")
clock = pygame.time.Clock()

# Ball class
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.randint(150, 300)
        self.vy = random.randint(150, 300)
        self.gravity = 980
        self.radius = 40

    def draw(self):
        pygame.draw.circle(screen, "black", (int(self.x), int(self.y)), self.radius)

    def update(self, dt):
        #Applying Gravity
        self.vy += self.gravity * dt
        # Move horizontally
        self.x += self.vx * dt
        # Move vertically
        self.y += self.vy * dt

        # Bounce off bottom
        if self.y >= HEIGHT - self.radius:
            self.y = HEIGHT - self.radius
            self.vy = -self.vy

        # Bounce off walls
        if self.x < self.radius or self.x > WIDTH - self.radius:
            self.vx = -self.vx

#Paddle Class
class Paddle(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move_h(self, speed):
        self.rect.x += speed

    def move_v(self, speed):
        self.rect.y += speed

# Create paddle
paddling = Paddle(paddle, 10, 503)
p = pygame.sprite.Group()
p.add(paddling)

# Create balls
b1 = Ball(780, 40)

# Game loop
running = True
while running:
    dt = clock.tick(60) / 1000
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle key input
    keys = pygame.key.get_pressed()
    if keys[K_RIGHT]:
        paddling.move_h(5)
    if keys[K_LEFT]:
        paddling.move_h(-5)
    if keys[K_UP]:
        paddling.move_v(-5)
    if keys[K_DOWN]:
        paddling.move_v(5)

    screen.blit(bg, (0,0))
    p.draw(screen)

    # Update and draw balls
    b1.update(dt)
    b1.draw()

    pygame.display.flip()

pygame.quit()
