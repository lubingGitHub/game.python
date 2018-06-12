import pygame


def log(*args, **kw):
    print(*args, **kw)

def rectIntersects(a, b):
    if b.y > a.y and b.y < a.y + a.imageHeight:
        if b.x > a.x and b.x < a.x + a.imageWidth:
            return True
    return False


# 使图片只载入一次
def images():
    d = {
        'block': 'image/block.png',
        'paddle': 'image/paddle.png',
        'ball': 'image/ball.png',
    }
    return d

def loadimages():
    image_dict = images()
    d = {}
    for k, v in image_dict.items():
        path = image_dict[k]
        img = pygame.image.load(path).convert_alpha()
        d[k] = img
    return d

def image_by_name(imageName):
    images = loadimages()
    img = images[imageName]
    return img