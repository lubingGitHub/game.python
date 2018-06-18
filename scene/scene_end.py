import pygame
from sys import exit
from scene.scene_basic import SceneBasic


class SceneEnd(SceneBasic):
    def __init__(self):
        super().__init__()
        self.actions = {
            pygame.K_ESCAPE: exit,
            pygame.K_r: self.transited,
        }

    def draw_tips(self):
        self.game.drawTips('press R to restart', 150, 150)

