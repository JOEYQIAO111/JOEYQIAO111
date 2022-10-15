'''# customize square
import turtle
p = turtle.Pen()
a = int(input("type the length of the square then press return:"))
for i in range(4):
    p.fd(a)
    p.right(90)
turtle.done()'''

# customize normal star
import turtle
s = turtle.Pen()
s.color("red")
for i in range(5):
    s.forward(100)
    s.right(140)
    s.forward(100)
    s.left(68)
turtle.done()