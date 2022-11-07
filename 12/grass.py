from pico2d import *

class Grass:
    def __init__(self, y = 30):
        self.image = load_image('grass.png')
        self.y = y
    def update(self):
        pass

    def draw(self):
        self.image.draw(400, self.y)


