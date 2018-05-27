import pygame
from pygame.locals import *
from sys import exit
from scene_package.paddle import Paddle
from scene_package.ball import Ball
from guagame import Guagame
from scene_package.level import loadLevel
from slider import slider_button

def gameRun():
    game = Guagame()
    paddle = Paddle()
    ball = Ball()
    paused = False
    # 这里不能注释， 有局部变量问题
    blocks = []

    actions = {
        pygame.K_RIGHT: paddle.moveRight,
        pygame.K_LEFT: paddle.moveLeft,
        pygame.K_f: ball.fire,
    }

    keydowns = {}
    x_scroll = 55

    score = 0


    while True:
        cur = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused
                elif event.key == pygame.K_1:
                    blocks = loadLevel(1)
                elif event.key == pygame.K_2:
                    blocks = loadLevel(2)
                elif event.key == pygame.K_3:
                    blocks = loadLevel(3)
                else:
                    keydowns[event.key] = True
            elif event.type == KEYUP:
                keydowns[event.key] = False

        # 调用的注册的函数
        for k in keydowns:
            if keydowns[k]:
                if k in actions:
                    actions[k]()

        if paused is not True:
            ball.move()


        # 球和挡板相撞
        if paddle.collode(ball):
            ball.rebound()


        # 更新画面

        game.clear()
        game.draw(paddle)
        game.draw(ball)
        game.drawScore(score)

        # 鼠标移动 ball 的位置
        if click[0] == 1:
            if ball.hasPoint(cur[0], cur[1]):
                ball.x = cur[0] - (ball.imageWidth / 2)
                ball.y = cur[1] - (ball.imageHeight / 2)

        for b in blocks:
            if b.alive:
                game.draw(b)
            if b.collode(ball):
                b.kill()
                ball.rebound()
                score += 100

        if ball.y > paddle.y:
            break

        x_scroll = slider_button(game.screen, (190, 190, 190), x_scroll)
        pygame.draw.rect(game.screen, ((190, 190, 190)), [x_scroll - 5, 258, 10, 24])
        fps_clock = pygame.time.Clock()
        fps_clock.tick(x_scroll-10)


        pygame.display.update()

