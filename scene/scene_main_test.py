import pygame
from pygame.locals import *
from sys import exit
from scene_package.paddle import Paddle
from scene_package.ball import Ball
from scene.guagame_test import Guagame
from scene_package.level import load_level
from scene_package.slider import timer


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
        self.is_transited = False

        self.actions = {
            pygame.K_d: self.paddle.moveRight,
            pygame.K_a: self.paddle.moveLeft,
            pygame.K_f: self.ball.fire,
            pygame.K_ESCAPE: exit,
        }

        self.actions_num = {
            pygame.K_1: load_level(1),
            pygame.K_2: load_level(2),
            pygame.K_3: load_level(3),
        }

    def get_event(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == pygame.K_p:
                    self.paused = not self.paused
                else:
                    self.keydowns[event.key] = True
            elif event.type == KEYUP:
                self.keydowns[event.key] = False

    def paused(self):
        for event in pygame.event.get():
            if event.key == pygame.K_p:
                self.paused = not self.paused

    def action(self):
        # d = self.actions_num()
        # 调用的注册的函数
        for k in self.game.keydowns:
            print('actions')
            if self.game.keydowns[k]:
                if k in self.game.actions_num:
                    print('self.game.actions', self.game.actions)
                    self.game.actions[k]()
                elif k in self.game.actions_num:
                    self.blocks = self.game.actions_num[k]

    def draw(self):
        self.game.clear()
        self.game.draw_image(self.paddle)
        self.game.draw_image(self.ball)
        self.game.drawScore(self.score)

        for b in self.blocks:
            if b.alive:
                self.game.draw_image(b)

    def update(self):
        # for event in pygame.event.get():
        #     print('监听事件')
        #     if event.type == KEYDOWN:
        #         if event.key == pygame.K_p:
        #             self.paused = not self.paused

        if self.paused is not True:
            self.ball.move()

        # 球和挡板相撞
        if self.paddle.collode(self.ball):
            self.ball.rebound()

        for b in self.blocks:
            if b.collode(self.ball):
                b.kill()
                self.ball.rebound()
                self.score += 100

    def transited(self):
        if self.ball.y > self.paddle.y:
            self.is_transited = True

    def timer(self):
        self.x_scroll = timer(self.game.screen, self.x_scroll)
        pygame.display.update()

    def drag_ball(self):
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if click[0] == 1:
            if self.ball.has_point(cur[0], cur[1]):
                self.ball.x = cur[0] - (self.ball.imageWidth / 2)
                self.ball.y = cur[1] - (self.ball.imageHeight / 2)

    # def begin(self):
    #     while self.is_transited is False:
    #         self.get_event()
    #         self.action()
    #         self.draw()
    #         self.drag_ball()
    #         self.transited()
    #         self.update()
    #         self.timer()



