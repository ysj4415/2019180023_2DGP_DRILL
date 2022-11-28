import game_framework
from pico2d import *
import random
import server
import game_world

class Ball:
    image = None
    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(50, server.background.w - 50), random.randint(50, server.background.h - 50)


    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        self.image.draw(sx, sy)

    def set_background(self, bg):
        self.bg = bg
        self.x = self.bg.w / 2
        self.y = self.bg.h / 2

    def handle_collision(self, other, group):
        if group == 'boy:balls':
            game_world.remove_object(self)

    def update(self):
        pass


