from scene_package.utils import (
    rectIntersects,
    image_by_name,
                   )

class Block():
    def __init__(self, x=100, y=200, l=1):
        self.x = x
        self.y = y
        self.image = image_by_name('block')
        self.imageWidth = self.image.get_width()
        self.imageHeight = self.image.get_height()
        self.alive = True
        self.lives = l

    def kill(self):
        self.lives -= 1
        if self.lives < 1:
            self.alive = False

    def collode(self, ball):
        return self.alive and (rectIntersects(ball, self) or rectIntersects(self, ball))

