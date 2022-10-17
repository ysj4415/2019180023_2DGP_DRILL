import game_framework
from pico2d import *
import play_state

running = True
image = None

def enter():
    global image
    image = load_image('add_delete_boy.png')

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
                case pico2d.SDLK_j:
                    if len(play_state.boys) > 1: play_state.boys.pop()
                case pico2d.SDLK_k:
                    play_state.boys.append(play_state.Boy())







