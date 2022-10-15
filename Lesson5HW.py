import turtle
n = 4
r = int(input('Type the length of the first shape: '))
t =  turtle.Pen()
t.speed(0)
t.up()
t.goto(0,-50)
t.down()
def polygon(n):
    for u in range(12):
        t.begin_fill()
        t.right(30)
        for i in range(n):
            t.fd(r)
            t.left(360/n)
        n = n+1
    turtle.done()
polygon(n)