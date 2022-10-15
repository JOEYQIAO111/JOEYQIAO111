# triangle or square
import turtle
def triangle(color):
    t = turtle.Pen()
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(3):
        t.fd(100)
        t.left(120)
    t.end_fill()
    turtle.done()


def square(color):
    t = turtle.Pen()
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
        t.fd(100)
        t.left(90)
    t.end_fill()
    turtle.done()
a = input('Enter a shape: (triangle/square): ')
b = input('Enter a color: (red/green/blue): ')
if a == 'square':
    square(b)
elif a == 'triangle':
    triangle(b)
else:
    print('shape not found')