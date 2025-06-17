import pygame, random
from pygame.locals import*

pygame.font.init()
pygame.mixer.init()
WIDTH = 1000
HEIGHT = 563
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Project")
bg = pygame.image.load("vortex.jpg")
paddle = pygame.image.load("paddle.png")
ball = pygame.image.load("ball.png")
clock = pygame.time.Clock()
score = 0
font1 = pygame.font.SysFont("Comic Sans", 20)

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
        screen.blit(ball, (int(self.x) - ball.get_width() // 2, int(self.y) - ball.get_height() // 2))

    def update(self, dt):
        # Apply gravity
        self.vy += self.gravity * dt
        # Move horizontally
        self.x += self.vx * dt
        # Move vertically
        self.y += self.vy * dt

        # Bounce off bottom
        if self.y >= HEIGHT - self.radius:
            self.y = HEIGHT - self.radius
            self.vy = -self.vy        
        
        # Bounce off top
        if self.y <= 0 + self.radius:
            self.y = 0 + self.radius
            self.vy = +self.vy

        # Bounce off walls
        if self.x < self.radius or self.x > WIDTH - self.radius:
            self.vx = -self.vx


# Paddle Class
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

# Create ball
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
        paddling.move_h(7)
    if keys[K_LEFT]:
        paddling.move_h(-7)
    if keys[K_UP]:
        paddling.move_v(-7)
    if keys[K_DOWN]:
        paddling.move_v(7)

    screen.blit(bg, (0, 0))
    p.draw(screen)

    # Red line
    line = pygame.Rect(0, 558, 1000, 5)
    pygame.draw.rect(screen, "red", line)

    # Update ball
    b1.update(dt)

    #Score Deductions
    ball_rect = pygame.Rect(b1.x - b1.radius, b1.y - b1.radius, b1.radius * 2, b1.radius * 2)
    if ball_rect.colliderect(line):
        score -= 1

    if ball_rect.colliderect(paddling):
        score += 1
        b1.y -= b1.radius
        b1.vy = -b1.vy           

    # Draw ball and score
    b1.draw()
    scoretxt = font1.render("Score: " + str(score), True, "black")
    screen.blit(scoretxt, (10, 10))

    pygame.display.flip()

pygame.quit()
