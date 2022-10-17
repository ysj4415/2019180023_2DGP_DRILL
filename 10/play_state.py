from pico2d import *
import game_framework
import item_state
import add_delete_state
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(0,100), 90
        self.frame = 0
        self.dir = 1
        self.image = load_image('animation_sheet.png')
        self.item= None
        self.ball_image = load_image('ball21x21.png')
        self.big_ball_image = load_image('ball41x41.png')



    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 5
        if self.x > 800:
            self.x = 800
            self.dir = -1
        elif self.x < 0:
            self.x = 0
            self.dir = 1

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        elif self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        if self.item == 'Ball':
            self.ball_image.draw(self.x+10, self.y+50)
        if self.item == 'BigBall':
            self.big_ball_image.draw(self.x + 10, self.y + 50)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.quit()
                case pico2d.SDLK_i:
                    game_framework.push_state(item_state)
                case pico2d.SDLK_b:
                    game_framework.push_state(add_delete_state)


boys = []
glass = None
# running = True


# 초기화
def enter():
    global boys, grass, running
    boys.append(Boy())
    grass = Grass()
    running = True

# 종료
def exit():
    global boys, grass
    del boys
    del grass

# 월드에 존재하는 객체들을 업데이트
def update():
    for boy in boys : boy.update()
    # grass 는 update x

def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def draw_world():
    grass.draw()
    for boy in boys : boy.draw()


def pause():
    pass

def resume():
    pass
