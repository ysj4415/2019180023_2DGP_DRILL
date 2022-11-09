from pico2d import *

import game_framework
import game_world
from ball import Ball

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14


PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 40.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)



class Bird:

    def __init__(self,x = 100 ,y = 200):
        self.x, self.y = x, y
        self.frame = 0
        self.dir = 1
        self.image = load_image('bird_animation.png')

        self.font = load_font('ENCR10B.TTF', 16)
    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        if self.x >= 1500:
            self.dir = -1
        elif self.x <= 100:
            self.dir = 1




    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw(int(self.frame) % 5 * 182, (2 - int(self.frame) // 5) * 168, 182, 168, 0, '', self.x, self.y, 91, 84)
        else:
            self.image.clip_composite_draw(int(self.frame) % 5 * 182, (2 - int(self.frame) // 5) * 168, 182, 168, 0, 'h', self.x, self.y, 91, 84)



