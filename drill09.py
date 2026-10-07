from pico2d import *

CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 1024


def handle_events():
    global running
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False


def draw():
    clear_canvas()
    ground.draw(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2)
    update_canvas()


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
ground = load_image('TUK_GROUND.png')

running = True

while running:
    handle_events()
    draw()
    delay(0.05)

close_canvas()
