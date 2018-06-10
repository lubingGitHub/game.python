# from scene import gameRun
from scene_title import gameStart
from scene_copy import gamerun
from scene_title_copy import gametitle
from scene_end_copy import gameend


def run():
    while True:
        # gameStart()
        gametitle()
        gamerun()
        gameend()


if __name__ == '__main__':
    run()