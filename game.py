from go.game_run import gamerun
# from go.game_title import gametitle
from go.game_end import gameend
from scene.guagame_test import Guagame
from scene.scene_main_test import Scene
from scene.scene_title_test import SceneTitle


def run():
    # while True:
        # gametitle()
        gua_game = Guagame()
        scene = SceneTitle()
        gua_game.replace_scene(scene)
        gua_game.begin()


if __name__ == '__main__':
    run()