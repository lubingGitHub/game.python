from go.game_run import gamerun
from go.game_title import gametitle
from go.game_end import gameend


def run():
    while True:
        gametitle()
        gamerun()
        gameend()


if __name__ == '__main__':
    run()