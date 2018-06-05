import pygame
from pygame.locals import *
from sys import exit
from scene_package.paddle import Paddle
from scene_package.ball import Ball
from guagame import Guagame
from scene_package.level import loadLevel
from scene_package.slider import slider_button


class Scene():
    def __init__(self):
        self.game = Guagame()
        self.paddle = Paddle()
        self.ball = Ball()
        self.paused = False
        self.score = 0
        self.keydowns = {}
        self.x_scroll = 55
        self.blocks = []

        self.actions = {
            pygame.K_d: self.paddle.moveRight,
            pygame.K_a: self.paddle.moveLeft,
            pygame.K_f: self.ball.fire,
            pygame.K_ESCAPE: exit,
        }

        self.actions_num = {
            pygame.K_1: loadLevel(1),
            pygame.K_2: loadLevel(2),
            pygame.K_3: loadLevel(3),
        }




    def action(self):
        # 调用的注册的函数
        for k in self.keydowns:
            if self.keydowns[k]:
                if k in self.actions:
                    self.actions[k]()
                elif k in self.actions_num:
                    self.blocks = self.actions_num[k]

    def draw(self):
        self.game.clear()
        self.game.draw(self.paddle)
        self.game.draw(self.ball)
        self.game.drawScore(self.score)

        for b in self.blocks:
            if b.alive:
                self.game.draw(b)
            if b.collode(self.ball):
                b.kill()
                self.ball.rebound()
                self.score += 100

    def update(self):

        if self.paused is not True:
            self.ball.move()


        # 球和挡板相撞
        if self.paddle.collode(self.ball):
            self.ball.rebound()

    def timer(self):
        x_scroll = slider_button(self.game.screen, (190, 190, 190), self.x_scroll)
        self.x_scroll = x_scroll
        pygame.draw.rect(self.game.screen, ((190, 190, 190)), [self.x_scroll - 5, 258, 10, 24])
        fps_clock = pygame.time.Clock()
        fps_clock.tick(x_scroll - 10)
        # timer(game.screen, x_scroll)



