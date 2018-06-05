import pygame
from pygame.locals import *
from sys import exit
from guagame import Guagame



def gameOver():
    isRestart = False
    gameEnd = Guagame()

    while True:

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == pygame.K_r:
                    isRestart = True
                elif event.key == pygame.K_ESCAPE:
                    exit()


        if isRestart == True:
            break

        gameEnd.clear()
        gameEnd.drawTips('game over, press R to restart', 150, 150)

        pygame.display.update()

