import pygame
from pygame.locals import *
import random
import gamelib

class Escaping(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')
    YELLOW = pygame.Color('yellow')
    RED = pygame.Color('red')
    BLUE = pygame.Color('blue')
    AmountOfSquare = 3
    AmountOfMonster = 3
    HEIGHT = 630
    WIDTH = 480
    radius = 15

    def init(self):
        super(Escaping, self).init()

    
    def __init__(self):
        super(Escaping, self).__init__('Escaping', Escaping.BLACK)

    def update(self):
        pass

    def render(self, surface):
        pass

def main():
    game = Escaping()
    game.run()

if __name__ == '__main__':
    main()
