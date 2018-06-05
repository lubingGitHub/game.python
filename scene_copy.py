import pygame
from pygame.locals import *
from scene_basic import Scene

def gameRun():

    scene = Scene()

    while True:
        # cur = pygame.mouse.get_pos()
        # click = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == pygame.K_p:
                    scene.paused = not scene.paused
                else:
                    scene.keydowns[event.key] = True
            elif event.type == KEYUP:
                scene.keydowns[event.key] = False


        scene.action()

        scene.draw()
        scene.update()

        scene.timer()
        pygame.display.update()


        # if scene.ball.y > scene.paddle.y:
        #     break
