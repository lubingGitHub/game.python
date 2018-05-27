from scene_package.block import Block

def levels(n):
    levels = [
        [
            [0, 0, 0,],
        ],
        [
            [50, 0, 0,],
            [100, 100, 0,],
        ],
        [
            [50, 30, 0,],
            [100, 100, 2,],
            [200, 100, 2,],
        ],
    ]
    return levels[n]


def loadLevel(n):
    blocks = []
    n = n - 1
    level = levels(n)
    for i in range(len(level)):
        p = level[i]
        b = Block(p[0], p[1], p[2])
        blocks.append(b)
    return blocks


