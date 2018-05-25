import pygame

def log(*args, **kw):
    print(*args, **kw)



def rectIntersects(a, b):
    if b.y > a.y and b.y < a.y + a.imageHeight:
        if b.x > a.x and b.x < a.x + a.imageWidth:
            return True
    return False


def images():
    d = {
        'block': 'image/block.png',
        'paddle': 'image/paddle.png',
        'ball': 'image/ball.png',
        'ball1': 'image/ball1.png',

    }
    return d

def loadimages():
    image = images()
    d = {}
    for k, v in image.items():
        path = image[k]
        img = pygame.image.load(path).convert_alpha()
        d[k] = img
    return d

def imageByName(imageName):
    images = loadimages()
    img = images[imageName]
    return img