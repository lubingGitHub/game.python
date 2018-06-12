from scene_package.utils import image_by_name
# 侧面撞，相交的矩形的x，y 和ball 的纵坐标速度和横坐标速度比


class Ball():
    def __init__(self, x=100, y=200, speed=10):
        self.x = x
        self.y = y
        self.speedX = speed
        self.speedY = speed
        self.image = image_by_name('ball')
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

    def has_point(self, x, y):
        return self.xIn(x) and self.yIn(y)

    def xIn(self, x):
        return x >= self.x and x <= self.x + self.imageWidth

    def yIn(self, y):
        return y >= self.y and y <= self.y + self.imageHeight
