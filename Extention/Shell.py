import turtle
t = turtle.Pen()
n = 0.1
turtle.screensize(10000,10000)
turtle.tracer(False)
t.up()
t.goto(0,-400)
t.down()
def shell(n):
    for i in range(250):
        t.circle(n)
        n = n+5
    turtle.done()
shell(n)