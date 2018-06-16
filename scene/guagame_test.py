import pygame
from pygame.locals import *


class Guagame():
    pygame.init()
    pygame.display.set_caption("打砖块")

    def __init__(self):
        self.screen = pygame.display.set_mode((400,300))
        self.scene = None
        self.keydowns = {}
        self.actions = {}
        self.actions_num = {}

    def clear(self):
        self.screen.fill((255, 255, 255))

    def draw_image(self, image):
        self.screen.blit(image.image, (image.x, image.y))

    def drawScore(self, score):
        score = 'score: ' + str(score)
        self.drawTips(score, 300, 260)

    def drawTips(self, text, x, y):
        # 创建字体对象
        font = pygame.font.Font(None, 20)
        # 文本与颜色
        text = font.render(text, 50, (0, 0, 0))
        self.screen.blit(text, (x ,y))

    def draw(self):
        self.scene.draw()

    def update(self):
        self.scene.update()

    def replace_scene(self, scene):
        self.scene = scene

    # def get_event(self):
    #     for event in pygame.event.get():
    #         if event.type == KEYDOWN:
    #             self.scene.keydowns[event.key] = True
    #         elif event.type == KEYUP:
    #             self.scene.keydowns[event.key] = False

    def action(self):
        # d = self.actions_num()
        # 调用的注册的函数
        for k in self.scene.keydowns:
            if self.scene.keydowns[k]:
                if k in self.scene.actions:
                    self.scene.actions[k]()
                elif k in self.scene.actions_num:
                    self.scene.blocks = self.scene.actions_num[k]

    def begin(self):
        while self.scene.is_transited is False:
            self.scene.get_event()
            self.action()
            self.draw()
            self.scene.drag_ball()
            # self.scene.transited()
            self.update()
            self.scene.timer()

