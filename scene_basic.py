import pygame
from pygame.locals import *
from sys import exit
from scene_package.paddle import Paddle
from scene_package.ball import Ball
from guagame import Guagame
from scene_package.level import loadLevel
from scene_package.slider import slider_button


class SceneBasic:
    def __init__(self):
        self.is_transited = False
        self.game = Guagame()
        self.keydowns = {}
        self.actions = {
            pygame.K_ESCAPE: exit,
        }

    def get_event(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                self.keydowns[event.key] = True
            elif event.type == KEYUP:
                self.keydowns[event.key] = False

    def action(self):
        # 调用的注册的函数
        for k in self.keydowns:
            if self.keydowns[k]:
                if k in self.actions:
                    self.actions[k]()

    def transited(self):
        self.is_transited = True

    def draw(self):
        self.game.clear()

    def draw_tips(self, text, x, y):
        self.game.drawTips(text, x, y)

    def update(self):
        pygame.display.update()

    def begin(self, text, x, y):
        while self.is_transited is False:
            self.get_event()
            self.action()
            self.draw()
            self.draw_tips(text, x, y)
            self.update()
