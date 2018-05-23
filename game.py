import pygame
from pygame.locals import *
from sys import exit
from paddle import Paddle
from ball import Ball
from block import Block
from utils import log
from guagame import Guagame
from level import loadLevel
from slider import slider_button


def run():
    game = Guagame()
    paddle = Paddle()
    ball = Ball()
    paused = False
    # 这里不能注释， 局部变量
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

        game.clear()
        game.draw(paddle)
        game.draw(ball)
        game.textBlit(score)

        for i in range(len(blocks)):
            block = blocks[i]
            if block.alive:
                game.draw(block)
            if block.collode(ball):
                block.kill()
                ball.rebound()
                score += 100


        if click[0] == 1:
            log('在')
            if ball.hasPoint(cur[0], cur[1]):
                ball.x = cur[0]
                ball.y = cur[1]

        x_scroll = slider_button(game.screen, (190, 190, 190), x_scroll)
        pygame.draw.rect(game.screen, ((190, 190, 190)), [x_scroll - 5, 258, 10, 24])
        fps_clock = pygame.time.Clock()
        fps_clock.tick(x_scroll-10)

        print(click[0])
        print((cur[0]), cur[1])

        pygame.display.update()


if __name__ == '__main__':
    run()