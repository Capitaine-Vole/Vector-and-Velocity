import pygame
import math
 
pygame.init()
 
WIDTH, HEIGHT = 1080, 720
 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RANDOMED = (252, 153, 184)
 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Vector")
 
def getMousePos():
    return pygame.mouse.get_pos()
 
class Ball:
    def __init__(self, x , y, color, radius, mass=1, win=screen):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        #self.gravity = gravity
        #self.energy_loss = energy_loss
        self.mass = mass
        self.win = win
 
        self.x_vel = 0
        self.y_vel = 0
 
    def draw(self):
        pygame.draw.circle(self.win, self.color, (self.x, self.y), self.radius)
 
    def launchBall(self):
        dx = pygame.mouse.get_pos()[0] - self.x
        dy = pygame.mouse.get_pos()[1] - self.y
        """
        if dx < 0:
            dx *= -1
        if dy < 0:
            dy *= -1
        if dx >= 0:
            dx *= -1
        if dy >= 0:
            dy *= -1
        """
        
        angleA = math.atan2(dy, dx)
        angleO = math.atan2(dx, dy)
        xm = math.cos(angleA) * 10
        ym = math.sin(angleA) * 10
        x = self.x + dx * -1
        y = self.y + dy * -1
        print(x, y)
        #print(dm)
        pygame.draw.lines(self.win, BLACK, False, ((self.x, self.y), (x, y)), 2)
        pygame.draw.lines(self.win, BLACK, False, ((self.x, self.y), (x, self.y)), 2)
        pygame.draw.lines(self.win, BLACK, False, ((x, y), (x, self.y)), 2)
 
 
ball = Ball(WIDTH / 2, HEIGHT / 2, GREEN, 10)
 
clock = pygame.time.Clock()
run = True
while run:
 
    clock.tick(60)
    screen.fill(WHITE)
 
    ball.draw()
    ball.launchBall()
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            quit()
 
    pygame.display.update()