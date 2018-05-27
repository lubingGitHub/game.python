from scene import gameRun
from scene_end import gameOver
from scene_title import gameStart

def run():
    while True:
        gameStart()
        gameRun()
        gameOver()


if __name__ == '__main__':
    run()