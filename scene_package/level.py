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

def load(n):
    path = 'level/{}.txt'.format(n)
    with open(path, 'r') as f:
        lines = f.readlines()
        for b in lines:
            prop = b.split(', ')
            if len(prop) < 3:
                prop.append('0')
            x = int(prop[0])
            y = int(prop[1])
            live = int(prop[2])
            self.blocks_props.append((x, y, live))
