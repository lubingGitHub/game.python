from utils import imageFromPath


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

    def rebound(self):
        self.speedY *= -1