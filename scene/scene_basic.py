import pygame
from pygame.locals import *
from sys import exit
from scene.guagame import Guagame


class SceneBasic:
    def __init__(self):
        self.is_transited = False
        self.game = Guagame()
        print('basic', id(self.game), self.game)

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

    def update(self):
        pygame.display.update()

    def begin(self):
        while self.is_transited is False:
            self.get_event()
            self.action()
            self.draw()
            self.update()
