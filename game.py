import pygame
from pygame.locals import *
from sys import exit


def log(*args, **kw):
    print(*args, **kw)

def imageFromPath(path):
    img = pygame.image.load(path).convert_alpha()
    return img

class Paddle():
    def __init__(self, x=100, y=250, speed=15):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = imageFromPath('paddle.png')
        self.imageWidth = self.image.get_width()
        self.imageHeight = self.image.get_height()


    def moveLeft(self):
        self.x -= self.speed

    def moveRight(self):
        self.x += self.speed

    def collode(self, ball):
        if ball.y + ball.imageHeight > self.y:
            if ball.x > self.x and ball.x < self.x + self.imageWidth:
                return True

        return False

class Ball():
    def __init__(self, x=100, y=200, speed=10):
        self.x = x
        self.y = y
        self.speedX = speed
        self.speedY = speed
        self.image = imageFromPath('ball.png')
        self.fired = False
        self.imageWidth = self.image.get_width()
        self.imageHeight = self.image.get_height()

    def move(self):
        if self.fired:
            if self.x < 0 or self.x + self.imageWidth> 400:
                self.speedX *= -1
            if self.y < 0 or self.y + self.imageHeight> 300:
                self.speedY *= -1

            self.x += self.speedX
            self.y += self.speedY

    def fire(self):
        self.fired = True


class guagame():
    pygame.init()
    pygame.display.set_caption("打砖块")

    def __init__(self):
        self.screen = pygame.display.set_mode((400,300))

    def clear(self):
        self.screen.fill((255, 255, 255))

    def draw(self, image):
        self.screen.blit(image.image, (image.x, image.y))


def run():
    game = guagame()
    paddle = Paddle()
    ball = Ball()

    actions = {
        pygame.K_RIGHT: paddle.moveRight,
        pygame.K_LEFT: paddle.moveLeft,
        pygame.K_f: ball.fire
    }

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()



        key = pygame.key.get_pressed()
        for k in actions:
            if key[k]:
                actions[k]()

        ball.move()

        if paddle.collode(ball):
            ball.speedY *= -1

        game.clear()
        game.draw(paddle)
        game.draw(ball)

        fps_clock = pygame.time.Clock()
        fps_clock.tick(1000 / 30)

        pygame.display.update()


if __name__ == '__main__':
    run()