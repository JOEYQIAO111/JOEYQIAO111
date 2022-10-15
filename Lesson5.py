#Shell
import turtle
x = 2
t = turtle.Pen()
turtle.colormode(255)
turtle.tracer(False)
t.up()
t.goto(0,-420)
t.down()
def polygon(x):
    for u in range(100):
        x = x + 1
        for i in range(x):
            t.fd(25)
            t.left(360/x)
    turtle.done()
polygon(x)

'''import turtle
t = turtle.Pen()
t.speed(0)
x = 15
def square(x):
    for u in range(13):
        x = x+10
        for i in range(4):
            t.fd(x)
            t.right(90)
        t.right(30)
    turtle.done()
square(x)'''