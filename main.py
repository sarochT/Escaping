import pygame
from pygame.locals import *
import random
import gamelib
from elements import Square,Player,Monster

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
        self.render_score()
    
    def __init__(self):
        super(Escaping, self).__init__('Escaping', Escaping.BLACK)
        self.player = Player(radius=self.radius, color=Escaping.WHITE, pos=(self.window_size[0]/2, self.window_size[1]/2), vy = 120, check_jump = 0)
        self.squares = []
        self.monsters1 = []
        self.monsters2 = []
        self.monsters3 = []
        self.score = 0
        self.count_time = 0
        self.time = 0
        self.init_monster()
        self.IsGameStarted = True
        self.init_Square()
        
    def init_Square(self):
        for i in range(0, self.AmountOfSquare) :
            self.squares.append(Square(pos_y=self.HEIGHT/self.AmountOfSquare*i, color=Escaping.GREEN))

    def init_monster(self):
        for j in range(0, self.AmountOfMonster) :
            self.monsters1.append(Monster(radius=self.radius, color=Escaping.BLUE, 
                pos=(random.randint(0,self.WIDTH), self.HEIGHT/self.AmountOfSquare+15), vy=10, waytowalk=random.randint(0,1)))
        for j in range(0, self.AmountOfMonster) :
            self.monsters2.append(Monster(radius=self.radius, color=Escaping.GREEN, 
                pos=(random.randint(0,self.WIDTH), self.HEIGHT/self.AmountOfSquare*2+15), vy=10, waytowalk=random.randint(0,1)))
        for j in range(0, self.AmountOfMonster) :
            self.monsters3.append(Monster(radius=self.radius, color=Escaping.RED, 
                pos=(random.randint(0,self.WIDTH), self.HEIGHT/self.AmountOfSquare*3+15), vy=10, waytowalk=random.randint(0,1)))

    def update(self):
        if self.IsGameStarted :
            self.auto_move_Square()
            self.player.auto_move()
            self.update_CanPlayerJump()
            self.player.check_x()
            self.key_pressed()
            self.update_time()
            self.update_monster()
            self.CheckCollision_Between_Monster_Player()

    def update_monster(self):
        for y in self.monsters1 :
            y.auto_move(self.count_time, self.time)
        for y in self.monsters2 :
            y.auto_move(self.count_time, self.time)
        for y in self.monsters3 :
            y.auto_move(self.count_time, self.time)

    def auto_move_Square(self):
        for x in self.squares :
            x.auto_move()

    def CheckCollision_Between_Monster_Player(self):
        if self.time >= 4:
            for x in self.monsters1 :
                if self.player.crop.colliderect(x.crop):
                    self.IsGameStarted = False
                    print "collide"
        if self.time >= 8:
            for x in self.monsters2 :
                if self.player.crop.colliderect(x.crop):
                    self.IsGameStarted = False
                    print "collide"
        if self.time >= 1:
            for x in self.monsters3 :
                if self.player.crop.colliderect(x.crop):
                    self.IsGameStarted = False
                    print "collide"

    def update_time(self):
        self.time = self.count_time/60
        self.count_time += 1
        self.render_time()

    def update_CanPlayerJump(self):
         for x in self.squares :
            if self.player.crop.colliderect(x.crop) and self.player.check_jump == 0 :
                self.player.check_jump = 2
                self.score += 1
                self.render_score()

    def key_pressed(self):
        if self.is_key_pressed(K_LEFT):
            self.player.move_left()
        elif self.is_key_pressed(K_RIGHT):
            self.player.move_right()
        if self.is_key_pressed(K_SPACE):
            if self.player.check_jump == 2 :
                self.player.move_jump()

    def render(self, surface):
        self.player.render(surface)
        surface.blit(self.score_image, (10,10))
        surface.blit(self.time_image,(10,50))
        self.render_Monster(surface)
        self.render_Square(surface)

    def render_score(self):
        self.score_image = self.font.render("Score = %d" % self.score, 0, Escaping.WHITE)

    def render_time(self):
        self.time_image = self.font.render("Time : %d" % self.time, 0 , Escaping.WHITE)

    def render_Monster(self, surface):
        if self.time >= 4:
            for y in self.monsters1:
                y.render(surface)
        if self.time >= 8:
            for y in self.monsters2:
                y.render(surface)
        if self.time >= 1:
            for y in self.monsters3:
                y.render(surface)
    def render_Square(self, surface):
        for x in self.squares:
            x.render(surface)


def main():
    game = Escaping()
    game.run()

if __name__ == '__main__':
    main()
