import pygame

def log(*args, **kw):
    print(*args, **kw)

def imageFromPath(path):
    img = pygame.image.load(path).convert_alpha()
    return img

def rectIntersects(a, b):
    if b.y > a.y and b.y < a.y + a.imageHeight:
        if b.x > a.x and b.x < a.x + a.imageWidth:
            return True
    return False
