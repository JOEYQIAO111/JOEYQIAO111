'''import pgzrun

TITLE = 'Circle'

WIDTH = 600
HEIGHT = 600

a = 50

def draw():
    global a
    screen.draw.filled_circle((300, 300), a, color='red')

def update():
    global a
    if a < 200:
        a += 1

pgzrun.go()'''

import pgzrun
import random

TITLE = 'Circle'

WIDTH = 600
HEIGHT = 600

x, y = 300, 300
speed_x = random.randint(8,12)
speed_y = random.randint(8,12)

def draw():
    global x, y
    screen.draw.filled_circle((x, y), 50, color='red')

def update():
    global x, y, speed_x, speed_y
    screen.clear()

    x += speed_x
    if x >= WIDTH - 50 or x <= 50:
        speed_x = -speed_x

    y -= speed_y
    if y >= HEIGHT - 50 or y<= 50:
        speed_y = -speed_y

pgzrun.go()