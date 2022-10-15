# random square, triangle, circle, and cross
import turtle
import random
t = turtle.Pen()
t.width(3)
t.speed(0)

def filled_square(x,y,color):
    t.up()
    t.goto(x,y)
    t.down()
    t.color(color)
    t.begin_fill()
    for i in range(4):
        t.fd(60)
        t.lt(90)
    t.end_fill()

def filled_circle(x,y,color):
    t.up()
    t.goto(x,y)
    t.down()
    t.color(color)
    t.begin_fill()
    t.circle(30)
    t.end_fill()

def filled_triangle(x,y,color):
    t.up()
    t.goto(x,y)
    t.down()
    t.color(color)
    t.begin_fill()
    for u in range(3):
        t.fd(60)
        t.left(120)
    t.end_fill()

def cross(x,y,color):
    t.up()
    t.goto(x,y)
    t.down()
    t.color(color)
    t.fd(60)
    t.backward(30)
    t.lt(90)
    t.fd(30)
    t.backward(60)

for r in range(50):
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    if x > 0 and y > 0:
        filled_triangle(x,y,'gold')
    if x < 0 and y < 0:
        filled_square(x,y,'blue')
    if x < 0 and y > 0:
        filled_circle(x,y,'green')
    if x > 0 and y < 0:
        cross(x,y,'red')

turtle.done()