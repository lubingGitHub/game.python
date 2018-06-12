from scene_package.utils import image_by_name


class Paddle():
    def __init__(self, x=100, y=250, speed=15):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = image_by_name('paddle')
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

    def aInb(self, x, x1, x2):
        return x >= x1 and x <= x2

    def collode(self, ball):
        if self.aInb(self.x, ball.x, ball.x + ball.imageWidth) or self.aInb(ball.x, self.x, self.x+self.imageWidth):
            if self.aInb(self.y, ball.y, ball.y + ball.imageHeight) or self.aInb(ball.y, self.y, self.y+self.imageHeight):
                return True
        return False