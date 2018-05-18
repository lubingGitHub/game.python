import pygame
from pygame.locals import *
from sys import exit


pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("打砖块")

# background = pygame.image.load(background_image_filename).convert()
paddle = pygame.image.load('paddle.png').convert_alpha()

x = 100
y = 250
speed = 5
leftDown = False
rightDown = False
fps_clock = pygame.time.Clock()

while True:
    # 游戏主循环


    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            if event.key == pygame.K_LEFT:
                leftDown = True
            elif event.key == pygame.K_RIGHT:
                rightDown = True
        elif event.type == KEYUP:
                leftDown = False
                rightDown = False

    # 这里不能放进 for 循坏
    # key = pygame.key.get_pressed()
    # if key[pygame.K_LEFT]:
    #     x -= 10
    # elif key[pygame.K_RIGHT]:
    #     x += 10


    if leftDown:
        x -= speed
    elif rightDown:
        x += speed

    screen.fill((255,255,255))
    fps_clock.tick(1000/30)
    screen.blit(paddle, (x,y))

    pygame.display.update()




 # screen.blit(background, (0, 0))
    # # 将背景图画上去
    #
    # x, y = pygame.mouse.get_pos()
    # # 获得鼠标位置
    # x -= mouse_cursor.get_width() / 2
    # y -= mouse_cursor.get_height() / 2
    # # 计算光标的左上角位置
    # screen.blit(mouse_cursor, (x, y))
    # 把光标画上去