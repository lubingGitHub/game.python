import pygame
from sys import exit
from test.scene_basic_test import SceneBasic
from test.scene_main_test import Scene


class SceneTitle(SceneBasic):
    def __init__(self):
        super().__init__()
        self.actions = {
            pygame.K_ESCAPE: exit,
            pygame.K_k: self.transited,
        }

    def transited(self):
        scene = Scene()
        self.game.replace_scene(scene)
        self.game.begin()

    def draw_tips(self):
        self.drawTips('press K to start', 150, 150)

    def update(self):

        self.draw_tips()
        pygame.display.update()





