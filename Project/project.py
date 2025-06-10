import pygame, random
from pygame.locals import*

pygame.font.init()
pygame.mixer.init()
WIDTH=1000
HEIGHT=563
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Project")    #title for the window
bg=pygame.image.load("vortex.jpg")
clock = pygame.time.Clock()

# Ball class
class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = random.randint(150, 300)
        self.vy = random.randint(150, 300)
        self.up = 0
        self.radius = 40

    def draw(self):
        pygame.draw.circle(screen, "black", (int(self.x), int(self.y)), self.radius)

    def update(self, dt):
        # Move horizontally
        self.x += self.vx * dt
        # Move vertically
        self.y += self.vy * dt

        # Bounce off bottom
        if self.y >= HEIGHT - self.radius:
            self.y = HEIGHT - self.radius
            self.up = self.up * dt

        # Move horizontally
        self.x += self.vx * dt

        # Bounce off walls
        if self.x < self.radius or self.x > WIDTH - self.radius:
            self.vx = -self.vx

        screen.blit(bg, (0,0))


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
    if keys[pygame.K_SPACE]:
        b1.up = -500

    # Update and draw balls
    b1.update(dt)
    b1.draw()

    pygame.display.flip()

pygame.quit()
