import pygame

pygame.init()

WIDTH, HEIGHT = 1080, 720

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball bounding")

class Ball:
    def __init__(self, x, y, color, radius, mass, win=screen):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.mass = mass
        self.win = win

        self.y_vel = 0
        self.x_vel = 0

    def draw(self):
        pygame.draw.circle(self.win, self.color, (self.x, self.y), self.radius)

    def updatePos(self, gravity, energy_loss):

        self.y_vel += gravity * self.mass
        self.y += self.y_vel

        self.x += self.x_vel

        if self.y > HEIGHT:
            self.y_vel = -self.y_vel * energy_loss
        if self.y < 0:
            self.y_vel = -self.y_vel * energy_loss

        if self.x > WIDTH:
            self.x_vel = self.x_vel * -1
        if self.x < 0:
            self.x_vel = self.x_vel * -1



ball = Ball(WIDTH / 2, HEIGHT / 2, GREEN, 20, 4)
ball.y_vel = 5

ball2 = Ball(WIDTH / 2, HEIGHT / 2, BLACK, 20, 2)
ball2.y_vel = 2
ball2.x_vel = 15

gravity = 0.05
energy_loss = 0.95

clock = pygame.time.Clock()
run = True

while run:

    clock.tick(60)
    screen.fill(WHITE)

    ball.draw()
    ball.updatePos(gravity, energy_loss)

    ball2.draw()
    ball2.updatePos(gravity, energy_loss)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            quit()

    pygame.display.update()