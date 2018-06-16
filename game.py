from go.game_run import gamerun
from go.game_title import gametitle
from go.game_end import gameend
from scene.guagame_test import Guagame
from scene.scene_main_test import Scene



def run():
    while True:
        gametitle()
        gua_game = Guagame()
        scene = Scene()
        gua_game.replace_scene(scene)
        gua_game.begin()
        # gamerun()
        gameend()


if __name__ == '__main__':
    run()