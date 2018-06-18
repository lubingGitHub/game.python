import pygame
from sys import exit
from test.scene_basic_test import SceneBasic
# from scene.scene_title_test import SceneTitle
from scene import SceneTitle


class SceneEnd(SceneBasic):
    def __init__(self):
        super().__init__()
        self.actions = {
            pygame.K_ESCAPE: exit,
            pygame.K_r: self.transited,
        }

    def draw_tips(self):
        self.drawTips('press R to restart', 150, 150)

    def transited(self):
        scene = SceneTitle()
        self.game.replace_scene(scene)
        self.game.begin()

    def update(self):
        self.draw_tips()
        pygame.display.update()

