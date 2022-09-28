from pico2d import *
import math
open_canvas()
grass = load_image('grass.png')
character = load_image('sprite_sheet.png')


cur_locationX = 30  #현재위치의 x좌표


def DrawAnim(frame, anim_step, x, y):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 70, anim_step, 70, 70, x, y)
    update_canvas()
    delay(0.07)
    get_events()


def Walking_anim(move_x):       #move_x만큼 이동
    frame = 0
    DrawAnim(frame, 71 * 11, cur_locationX, 79)

    for x in range(cur_locationX, cur_locationX + move_x, 5):
        DrawAnim(1 + frame,  71 * 11, x, 79)
        frame = (frame + 1) % 8
    return x



def Runnning_anim(move_x):
    frame = 0
    for x in range(cur_locationX, cur_locationX + move_x, 9):
        DrawAnim(6 + frame, 71 * 5, x, 79)
        frame = (frame + 1) % 6
    return x

def DownMove_anim(move_x):
    DrawAnim(0, 71 * 10, cur_locationX, 79)

    frame = 0
    for x in range(cur_locationX, cur_locationX + move_x, 2):
        DrawAnim(1 + frame, 71 * 10, x, 79)
        frame = (frame + 1) % 3
    return x

def QuickDownMove_anim(move_x):
    DrawAnim(4, 71 * 10, cur_locationX, 79)

    frame = 0
    for x in range(cur_locationX, cur_locationX + move_x, 5):
        DrawAnim(5 + frame, 71 * 10, x, 79)
        frame = ((frame + 1) % 7)
    return x

def CrossWall_anim():
    x = cur_locationX
    dig = 0
    for frame in range(0, 11):
        y = 79 + (15 * math.sin(dig * math.pi / 180))
        dig += 180 / 11
        DrawAnim(frame, 71 * 9, x, y)
        x += 5
    return x

def CrossWall2_anim():
    x = cur_locationX
    dig = 0
    for frame in range(0, 23):
        y = 79 + (15 * math.sin(dig * math.pi / 180))
        if dig < 180:
            dig += 180 / 17
        if frame <= 11:
            DrawAnim(frame, 71 * 8, x, y)
        else:
            DrawAnim(frame % 11, 71 * 7, x, y)
        x += 5
    return x

def BackWalking_anim(move_time):
    frame = 0

    for move in range(0, move_time):
        DrawAnim(frame, 71 * 6, cur_locationX, 79)
        frame = (frame + 1) % 6

def BackRunning_anim(move_time):
    frame = 0

    for move in range(0, move_time):
        DrawAnim(frame, 71 * 5, cur_locationX, 79)
        frame = (frame + 1) % 6

def ForwardWalking_anim(move_time):
    frame = 0

    for move in range(0, move_time):
        DrawAnim(6 + frame, 71 * 6, cur_locationX, 79)
        frame = (frame + 1) % 6

def ClimbingWall_anim(move_time):
    frame = 0
    y = 79
    for move in range(0, move_time):
        y += 5

        DrawAnim(frame, 72 * 4, cur_locationX, y)
        frame = (frame + 1) % 10


def Jump_anim():
    x = cur_locationX
    dig = 0
    for frame in range(0, 7):
        y = 79 + (40 * math.sin(dig * math.pi / 180))

        dig += 180 / 7

        DrawAnim(frame, 72 * 3, x, y)
        x += 5
    return x

def HighJump_anim():
    x = cur_locationX
    dig = 0
    for frame in range(0, 12):
        y = 79 + (70 * math.sin(dig * math.pi / 180))

        dig += 180 / 12

        DrawAnim(frame, 72 * 2, x, y)
        x += 5
    return x

def Ghost_anim(move_x):
    for y in range(79, 100):
        DrawAnim(7, 72 * 3, cur_locationX, y)
    frame = 0
    for x in range(cur_locationX, cur_locationX + move_x, 11):
        DrawAnim(frame, 72 * 1, x, 79)
        frame = (frame + 1) % 9
    return x



while True:
    cur_locationX = Walking_anim(200) % 800
    cur_locationX = Runnning_anim(200) % 800
    cur_locationX = DownMove_anim(100) % 800
    cur_locationX = QuickDownMove_anim(300) % 800
    cur_locationX = CrossWall_anim() % 800
    cur_locationX = CrossWall2_anim() % 800
    BackWalking_anim(30)
    BackRunning_anim(30)
    ForwardWalking_anim(30)
    ClimbingWall_anim(30)
    for r in range(3):
        cur_locationX = Jump_anim() % 800
        cur_locationX = HighJump_anim() % 800
    cur_locationX = Ghost_anim(200) % 800


close_canvas()