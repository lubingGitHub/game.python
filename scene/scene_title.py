import pygame
from pygame.locals import *
from sys import exit
from scene.guagame import Guagame
from scene.scene_basic import SceneBasic


class SceneTitle(SceneBasic):
    def __init__(self):
        super().__init__()
        self.actions = {
            pygame.K_ESCAPE: exit,
            pygame.K_k: self.transited,
        }

    def get_event(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == pygame.K_k:
                    self.transited()
                elif event.key == pygame.K_ESCAPE:
                    exit()

    def draw_tips(self):
        self.game.drawTips('press K to start', 150, 150)

    def begin(self):
        while self.is_transited is False:
            self.get_event()
            self.action()
            self.draw()
            self.draw_tips()
            self.update()






#
#
# def gameStart():
#     isStart = False
#     gameStart = Guagame()
#
#
#     while True:
#         for event in pygame.event.get():
#             if event.type == KEYDOWN:
#                 if event.key == pygame.K_k:
#                     isStart = True
#                 elif event.key == pygame.K_ESCAPE:
#                     exit()
#
#
#         if isStart is True:
#             break
#
#
#         gameStart.clear()
#         gameStart.drawTips('press K to start', 150, 150)
#
#         pygame.display.update()

