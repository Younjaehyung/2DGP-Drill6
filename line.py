import math
from pico2d import *
import random
TUK_WIDTH, TUK_HEIGHT = 1280, 1024


open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
arrow = load_image('hand_arrow.png')


def arrow_point():
    global mx,my
    arrow.draw(mx,my)



def handle_events():
    global x, y
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False


    pass

def random_cursor():
    global mx,my
    mx=random.randint(0,1280)
    my= random.randint(0, 1024)

def goto_cursor(p1, p2):
    # fill here
    global mx,my,xp,yp
    global t

    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]



    t+=1
    i=t/200


    x=((1-i)*x1)+(i*x2)
    y=((1-i)*y1)+(i*y2)
    if x>mx:
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
    elif x < mx:
        character.clip_draw(frame * 100, 100, 100, 100,x, y)

    delay(0.02)

    if t == 200:
        t = 0
        random_cursor()
        xp=x
        yp=y






# fill here

running = True
xp, yp = 0,0
x,y = TUK_WIDTH // 2, TUK_HEIGHT // 2
mx,my=0,0
frame = 0
t=0
hide_cursor()
random_cursor()
while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    arrow_point()
    goto_cursor((xp,yp),(mx,my))
    update_canvas()
    frame = (frame + 1) % 8
    handle_events()

