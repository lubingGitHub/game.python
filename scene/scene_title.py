import pygame
from sys import exit
from scene.scene_basic import SceneBasic


class SceneTitle(SceneBasic):
    def __init__(self):
        super().__init__()
        self.actions = {
            pygame.K_ESCAPE: exit,
            pygame.K_k: self.transited,
        }

    def draw_tips(self):
        self.game.drawTips('press K to start', 150, 150)






