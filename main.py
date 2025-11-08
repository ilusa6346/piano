from pygame import *
from setting import *
from keys import create_key_rects, draw_keys
init()
screen = display.set_mode((WIDTH, HEIGHT))
running = True
pressed = set()
key_rects = create_key_rects(7)
while running:
    for e in event.get():
        if e.type == QUIT:
            rinning = False
        screen.fill(WHITE)
        display.update()
        if e.type == KEYDOWN:
            if k in sound:
                sound[k].play()
                pressed.add(keys_list.index(k))
        if e.type == KEYUP:
            k = key.name(e.key)
            if k in keys:
                pressed.discard(keys_list.index(k)) 
        if e.type == MOUSEBUTTONDOWN:
            for i,r in enumerate(key_rects):
                if r.collidepoint(e.pos):
                    sound[keys_list[i]].play()
                    pressed.add(i)
        if e.type == MOUSEBUTTONUP:
            for i,r in enumerate(key_rects):
                if i in pressed and r.collidepoint(e.pos):
                    pressed.remove(i)

