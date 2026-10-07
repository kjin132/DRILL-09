from pico2d import *

CANVAS_WIDTH = 1280
CANVAS_HEIGHT = 1024


open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

running = True

while running:
    for event in get_events():
        if event.type == SDL_QUIT:
            running = False
    delay(0.05)

close_canvas()
