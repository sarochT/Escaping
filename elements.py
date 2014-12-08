import pygame
from pygame.locals import *
import random
class Square(object):

    THICKNESS = 10
    HEIGHT = 630
    WIDTH = 480

    def __init__(self, pos_y, color):
        self.pos_y = pos_y
        self.color = color
        self.crop = Rect((0, self.HEIGHT-self.pos_y, self.WIDTH, self.THICKNESS))

    def auto_move(self):
        self.pos_y  -= 1
        self.crop = Rect((0, self.HEIGHT-self.pos_y, self.WIDTH, self.THICKNESS))
        if self.HEIGHT - self.pos_y > self.HEIGHT :
            self.pos_y = self.HEIGHT

    def render(self, surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(0, self.HEIGHT-self.pos_y, self.WIDTH, self.THICKNESS),2)

#########################################

class Player(object):

    THICKNESS = 1
    HEIGHT = 630
    WIDTH = 480
    POWERTOJUMP = 210
    ERROR_SIZE = 5
    VX = 5

    def __init__(self, radius, pos, color, vy, check_jump):
        (self.x, self.y) = pos
        self.radius = radius
        self.color = color
        self.vy = vy
        self.check_jump = check_jump
        self.crop = Rect((self.x, self.HEIGHT - self.y - self.ERROR_SIZE,self.radius*2,self.radius*2))

    def auto_move(self):
        self.crop = Rect((self.x, self.HEIGHT - self.y - self.ERROR_SIZE,self.radius*2,self.radius*2))
        if self.check_jump == 1 :
            self.y += 1 + self.vy/30
            self.vy -= 3
            if self.vy <= 0 :
                self.check_jump = 0
        elif self.check_jump == 0 :
            self.y -= (1 + self.vy/20)
            self.vy += 3
        elif self.check_jump == 2 :
            self.y -= 1

    def check_x(self):
        if self.x < 0 :
            self.x = self.WIDTH-10
        elif self.x > self.WIDTH :
            self.x = 10
        

    def move_left(self):
        self.x -= self.VX

    def move_right(self):
        self.x += self.VX

    def move_jump(self):
        self.check_jump = 1
        self.vy = self.POWERTOJUMP

    def render(self, surface):
        pos = (int(self.x), self.HEIGHT - int(self.y))
        pygame.draw.circle(surface, self.color, pos, self.radius, 0)

#########################################

class Monster(object):

    THICKNESS = 1
    HEIGHT = 630
    WIDTH = 480
    RADIUS = 15
    VX  = 1
    VY = 1
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')
    YELLOW = pygame.Color('yellow')
    RED = pygame.Color('red')
    BLUE = pygame.Color('blue')
    Time = 0

    def __init__(self, radius, pos, color, vy , waytowalk):
        (self.x, self.y) = pos
        self.radius = radius
        self.waytowalk = waytowalk
        self.color = color
        self.vy = vy
        self.crop = Rect((self.x, self.HEIGHT - self.y, self.RADIUS*2, self.RADIUS*2))

    def auto_move(self, timeMS, time):
        self.VX += timeMS/1000000.0000000
        if time - self.Time > random.randint(5,12):
            self.waytowalk = random.randint(0,1)
            self.Time = time
        if self.waytowalk == 1:
            self.x -= self.VX
            self.y -= self.VY
            if self.x <= 0:
                self.waytowalk = 0
        elif self.waytowalk == 0:
            self.x += self.VX
            self.y -= self.VY
            if self.x >= self.WIDTH:
                self.waytowalk = 1
        if self.HEIGHT-self.y > self.HEIGHT :
            self.y = self.HEIGHT
            self.x = random.randint(0,self.WIDTH)
        self.crop = Rect((self.x, self.HEIGHT - self.y, self.RADIUS*2, self.RADIUS*2))

    def render(self, surface):
        pos = (int(self.x), self.HEIGHT - int(self.y))
        pygame.draw.circle(surface, self.color, pos, self.radius, 0)

############################################################

class Coin(object):

    THICKNESS = 1
    HEIGHT = 630
    WIDTH = 480
    RADIUS = 5
    VY = 1
    YELLOW = pygame.Color('yellow')


    def __init__(self, pos):
        (self.x, self.y) = pos
        self.crop = Rect((self.x, self.HEIGHT - self.y, self.RADIUS*2, self.RADIUS*2))

    def auto_move(self):
        self.y -= 1
        self.crop = Rect((self.x, self.HEIGHT - self.y, self.RADIUS*2, self.RADIUS*2))

    def render(self, surface):
        if self.HEIGHT - self.y > 0:
            pos = (int(self.x), self.HEIGHT - int(self.y))
            pygame.draw.circle(surface, self.YELLOW, pos, self.RADIUS, 0)
