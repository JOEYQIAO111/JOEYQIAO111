import turtle
t = turtle.Pen()
t.pencolor("blue")
t.width(8)

def circle():
    t.circle(80)

circle()
t.up()
t.goto(-60,60)
t.down()

def D():
    t.left(90)
    t.fd(40)
    t.backward(40)
    t.right(90)
    t.circle(20,180)

D()
t.up()
t.right(180)
t.fd(30)
t.right(90)
t.fd(10)
t.down()

def E():
    t.left(30)
    t.fd(30)
    t.left(90)
    t.fd(20)
    t.backward(20)
    t.left(90)
    t.fd(15)
    t.right(90)
    t.fd(20)
    t.backward(20)
    t.left(90)
    t.fd(15)
    t.right(90)
    t.fd(20)

E()
t.right(30)
t.up()
t.fd(30)
t.down()

def L():
    t.right(90)
    t.fd(35)
    t.left(90)
    t.fd(15)

L()
t.up()
t.left(90)
t.fd(35)
t.right(90)
t.fd(20)
t.down()
L()
turtle.done()