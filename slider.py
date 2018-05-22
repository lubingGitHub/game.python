import pygame
from pygame.locals import *
from sys import exit

pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("打砖块")

white = (255, 255, 255)
grey = (190, 190, 190)
bar_x = 20
bar_y = 270
x_scroll1 = 55

def slider_button(active_colour):
    global x_scroll1
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.line(screen, active_colour, (10, 270), (110, 270))
    if 110 > cur[0] > 10 and 284 > cur[1] > 258:
        if click[0] == 1:
            x_scroll1 = cur[0]
    return x_scroll1



# while True:
#     # 获取光标位置
#     pos = pygame.mouse.get_pos()
#     # 获得鼠标按钮的状态
#     click = pygame.mouse.get_pressed()
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             exit()
#
#     screen.fill((255, 255, 255))
#
#     slider_button(grey)
#     pygame.draw.rect(screen, grey, [x_scroll1 - 5, bar_y - 12, 10, 24])
#
#     pygame.display.update()