import pygame
from pygame.locals import *
from sys import exit
from paddle import Paddle
from ball import Ball
from block import Block
from utils import log
from guagame import Guagame
from level import (levels,
                    )


def run():
    game = Guagame()

    paddle = Paddle()
    ball = Ball()
    paused = False


    # def loadLevel(n):
    #     blocks = []
    #     n = n - 1
    #     level = levels[n]
    #     for i in range(len(level)):
    #         p = level[i]
    #         b = Block(p[0], p[1])
    #         blocks.append(b)
    #     return blocks
    #
    # for i in range(3):
    #     b = Block()
    #     b.x = i*100
    #     b.y = 100
    #     blocks.append(b)
    blocks = []

    def loadLevel(n):
        blocks = []
        n = n - 1
        level = levels[n]
        for i in range(len(level)):
            p = level[i]
            b = Block(p[0], p[1], p[2])
            blocks.append(b)
        return blocks

    actions = {
        pygame.K_RIGHT: paddle.moveRight,
        pygame.K_LEFT: paddle.moveLeft,
        pygame.K_f: ball.fire,
    }

    keydowns = {}


    while True:
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

        for i in range(len(blocks)):
            block = blocks[i]
            if block.alive:
                game.draw(block)

        for i in range(len(blocks)):
            block = blocks[i]
            if block.collode(ball):
                block.kill()
                ball.rebound()

        fps_clock = pygame.time.Clock()
        fps_clock.tick(1000 / 30)

        pygame.display.update()


if __name__ == '__main__':
    run()