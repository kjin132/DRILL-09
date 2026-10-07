from pico2d import *

CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 1024
FRAME_SIZE = 100
SPEED = 10


def handle_events():
    global running, dir_x
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
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1


def update():
    global x, frame
    x += dir_x * SPEED

    frame = (frame + 1) % 8


def draw():
    clear_canvas()
    ground.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
    character.clip_draw(frame * FRAME_SIZE, 3 * FRAME_SIZE, FRAME_SIZE, FRAME_SIZE, x, y)
    update_canvas()


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2
frame = 0
dir_x = 0

while running:
    handle_events()
    update()
    draw()
    delay(0.05)

close_canvas()
