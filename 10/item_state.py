import game_framework
from pico2d import *
import play_state

running = True
image = None

def enter():
    global image
    image = load_image('item_select.png')

def exit():
    global image
    del image

def update():
    play_state.update()
    pass

def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(400,300)
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                case pico2d.SDLK_0:
                    for boy in play_state.boys: boy.item = None
                    game_framework.pop_state()
                case pico2d.SDLK_1:
                    for boy in play_state.boys: boy.item = 'Ball'
                    game_framework.pop_state()
                case pico2d.SDLK_2:
                    for boy in play_state.boys: boy.item = 'BigBall'
                    game_framework.pop_state()







