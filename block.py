from utils import (imageFromPath,
                    rectIntersects)

class Block():
    def __init__(self, x=100, y=200):
        self.x = x
        self.y = y
        self.image = imageFromPath('block.png')
        self.imageWidth = self.image.get_width()
        self.imageHeight = self.image.get_height()
        self.alive = True

    def kill(self):
        self.alive = False

    def collode(self, ball):
        return self.alive and (rectIntersects(ball, self) or rectIntersects(self, ball))