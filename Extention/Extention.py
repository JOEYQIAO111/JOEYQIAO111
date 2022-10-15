# Star
import turtle
n = 20
t = turtle.Pen()
def star(n):
    t.right(144)
    for i in range(19):
        t.fd(n)
        t.right(144)
        n = n + 15
    turtle.done()
star(n)

'''# Strange thing
import turtle 
t = turtle.Pen()
t.speed(0)
def circle():
    for i in range(360):
        t.fd(250)
        t.right(30)
        t.fd(30)
        t.right(47)
        t.fd(30)
        t.backward(30)
        t.right(5)
        t.fd(30)
        t.backward(30)
        t.lt(47)
        t.backward(30)
        t.lt(30)
        t.backward(250)
        t.right(3)
    turtle.done()
circle()'''

'''# Strange circle
import turtle 
t = turtle.Pen()
turtle.tracer(False)
def circle():
    for i in range(360):
        t.fd(225)
        t.right(30)
        t.fd(30)
        t.right(55)
        t.fd(40)
        t.backward(40)
        t.right(10)
        t.fd(40)
        t.backward(40)
        t.lt(65)
        t.backward(30)
        t.lt(30)
        t.backward(225)
        t.right(3)
    turtle.done()
circle()'''

'''# triangle circle
import turtle
t = turtle.Pen()
t.speed(0)
t.pencolor('gold')
for i in range(50):
    t.fd(250)
    t.right(123)
turtle.done()'''

'''# captain america shield
import turtle
t = turtle.Pen()
t.speed(1000)
t.ht()
t.up()
t.goto(0,-100)
t.down()
t.color('red')
t.begin_fill()
t.circle(200)
t.end_fill()
t.lt(90)
t.fd(50)
t.rt(90)
t.color('white')
t.begin_fill()
t.circle(150)
t.end_fill()
t.lt(90)
t.fd(50)
t.rt(90)
t.color('red')
t.begin_fill()
t.circle(100)
t.end_fill()
t.lt(90)
t.fd(50)
t.rt(90)
t.color('blue')
t.begin_fill()
t.circle(50)
t.end_fill()
t.up()
t.rt(180)
t.fd(46)
t.rt(90)
t.fd(68)
t.right(90)
t.down()
t.color('white')
t.begin_fill()
t.rt(1)
t.fd(35)
for i in range(5):
    t.lt(68)
    t.fd(35)
    t.rt(140)
    t.fd(35)
t.end_fill()
turtle.done()'''