from pico2d import *

CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 1024
FRAME_SIZE = 100
HALF = FRAME_SIZE // 2
MARGIN_Y = 100         # 화면 위아래 끝에서 안쪽으로 들어온 거리
SPEED = 10

RUN_LEFT = 0
RUN_RIGHT = 1
IDLE_LEFT = 2
IDLE_RIGHT = 3


def handle_events():
    global running, dir_x, dir_y
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1


def clamp(value, low, high):
    return max(low, min(value, high))


def select_action():
    moving = dir_x != 0 or dir_y != 0
    if moving:
        return RUN_RIGHT if face_right else RUN_LEFT
    return IDLE_RIGHT if face_right else IDLE_LEFT


def update():
    global x, y, frame, face_right, action
    x = clamp(x + dir_x * SPEED, HALF, CANVAS_WIDTH - HALF)
    y = clamp(y + dir_y * SPEED, HALF + MARGIN_Y, CANVAS_HEIGHT - HALF - MARGIN_Y)

    if dir_x > 0:
        face_right = True
    elif dir_x < 0:
        face_right = False

    action = select_action()

    frame = (frame + 1) % 8


def draw():
    clear_canvas()
    ground.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
    character.clip_draw(frame * FRAME_SIZE, action * FRAME_SIZE, FRAME_SIZE, FRAME_SIZE, x, y)
    update_canvas()


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2
frame = 0
dir_x, dir_y = 0, 0
face_right = True
action = IDLE_RIGHT

while running:
    handle_events()
    update()
    draw()
    delay(0.05)

close_canvas()
