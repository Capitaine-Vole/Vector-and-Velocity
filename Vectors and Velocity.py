import pygame
import math
import time
 
pygame.init()

seconds = time.time()

WIDTH, HEIGHT = 1080, 720
 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RANDOMED = (252, 153, 184)
 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Vector")

def timerr():
    pass
 
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

        self.mooving = 0
 
    def draw(self):
        pygame.draw.circle(self.win, self.color, (self.x, self.y), self.radius)
 
    def launchBall(self):
        dx = pygame.mouse.get_pos()[0] - self.x
        dy = pygame.mouse.get_pos()[1] - self.y
        
        #img = pygame.image.load("img/arrow.png")
        

        """
        angleA = math.atan2(dy, dx)
        angleO = math.atan2(dx, dy)
        hyp = math.sqrt(dx**2 + dy**2)
        xm = math.cos(angleA) * hyp
        ym = math.sin(angleA) * hyp
        
        x = self.x + dx * -1
        y = self.y + dy * -1
        print(x, y, hyp, xm, ym)
        """

        angleA = math.atan2(dy, dx)
        angleO = math.atan2(dx, dy)
        hyp = math.sqrt(dx**2 + dy**2)
        xm = math.cos(angleA) * 100
        ym = math.sin(angleA) * 100
        
        x = xm * -1 + self.x
        y = ym * -1 + self.y

        #img = pygame.transform.scale(img, (100, 100))

        pygame.draw.lines(self.win, BLACK, False, ((self.x, self.y), (x, y)), 2)
        pygame.draw.lines(self.win, BLACK, False, ((self.x, self.y), (x, self.y)), 2)
        pygame.draw.lines(self.win, BLACK, False, ((x, y), (x, self.y)), 2)

        #self.win.blit(img, (self.x - 15, self.y - 50))

    def moove(self, mooving_pixels):
        dx = pygame.mouse.get_pos()[0] - self.x
        dy = pygame.mouse.get_pos()[1] - self.y
        angleA = math.atan2(dy, dx)
        angleO = math.atan2(dx, dy)
        hyp = math.sqrt(dx**2 + dy**2)
        
        xm = math.cos(angleA) * 1
        ym = math.sin(angleA) * 1

        self.x = xm * -1 + self.x
        self.y = ym * -1 + self.y

        pygame.draw.circle(self.win, self.color, (self.x, self.y), self.radius)
        time.sleep(0.1)
 
 
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
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                dx = pygame.mouse.get_pos()[0] - ball.x
                dy = pygame.mouse.get_pos()[1] - ball.y
                angleA = math.atan2(dy, dx)
                angleO = math.atan2(dx, dy)
                hyp = math.sqrt(dx**2 + dy**2)
                    
                xm = math.cos(angleA) * 1
                ym = math.sin(angleA) * 1

                ball.x = xm * -1 + ball.x
                ball.y = ym * -1 + ball.y
 
    pygame.display.update()