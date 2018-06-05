import pygame
from pygame.locals import *
from sys import exit
from guagame import Guagame




def gameStart():
    isStart = False
    gameStart = Guagame()


    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == pygame.K_k:
                    isStart = True
                elif event.key == pygame.K_ESCAPE:
                    exit()


        if isStart is True:
            break


        gameStart.clear()
        gameStart.drawTips('press K to start', 150, 150)

        pygame.display.update()

