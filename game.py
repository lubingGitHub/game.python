# from scene import gameRun
from scene_end import gameOver
from scene_title import gameStart
from scene_copy import gameRun


def run():
    while True:
        gameStart()
        gameRun()
        gameOver()


if __name__ == '__main__':
    run()