'''import turtle
t = turtle.Pen()
a = 10
def maze(a):
    for i in range(100):
        t.fd(a)
        t.rt(90)
        a = a + 5
    turtle.done()
maze(a)'''

'''import turtle
t = turtle.Pen()
length = 10
for i in range(60):
    t.fd(length)
    t.rt(91)
    length = length + 5
turtle.done()'''

'''import turtle
t = turtle.Pen()
t.speed(0)
turtle.colormode(255)
t.width(5)
for i in range(255,0,-3):
    t.color(255,i,0)
    t.fd(i)
    t.backward(i)
    t.rt(3)
turtle.done()'''

'''import turtle
def sqaure(i):
    for u in range(4):
        turtle.fd(i)
        turtle.lt(90)
for i in range(140,0,-20):
    sqaure(i)
turtle.done()'''

import turtle
for u in range(6):
    for i in range(4):
        turtle.fd(100)
        turtle.lt(90)
    turtle.lt(60)
turtle.done()