from scene_package.block import Block


# 重点是传给 Block类需要的参数
def load(n):
    path = 'level/level{}.txt'.format(n)
    with open(path, 'r') as f:
        l = []
        lines = f.readlines()
        for b in lines:
            b = b.replace('\n', '')
            prop = b.split(', ')
            if len(prop) < 3:
                prop.append('0')
            x = int(prop[0])
            y = int(prop[1])
            live = int(prop[2])
            l.append((x, y, live))
        return l


def load_level(n):
    levels = load(n)
    blocks = []
    for i in levels:
        # p = levels[i]
        b = Block(i[0], i[1], i[2])
        blocks.append(b)
    return blocks