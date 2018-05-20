from utils import imageFromPath


class Paddle():
    def __init__(self, x=100, y=250, speed=15):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = imageFromPath('paddle.png')
        self.imageWidth = self.image.get_width()
        self.imageHeight = self.image.get_height()

    def move(self, x):
        if x < 0:
            x = 0
        if x > 400 - self.imageWidth:
            x = 400 - self.imageWidth
        self.x = x

    def moveLeft(self):
        self.move(self.x - self.speed)

    def moveRight(self):
        self.move(self.x + self.speed)

    def collode(self, ball):
        if ball.y + ball.imageHeight > self.y:
            if ball.x > self.x and ball.x < self.x + self.imageWidth:
                return True

        return False