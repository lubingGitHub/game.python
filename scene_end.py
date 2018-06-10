import pygame
from pygame.locals import *
from sys import exit
from guagame import Guagame
from scene_basic import SceneBasic


class SceneEnd(SceneBasic):
    def __init__(self):
        super().__init__()
        self.actions = {
            pygame.K_ESCAPE: exit,
            pygame.K_r: self.transited,
        }

