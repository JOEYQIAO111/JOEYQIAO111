import turtle
a = int(input("type the length of the square:"))
p = turtle.Pen()
p.speed(100)
p.color("red")
for e in range(24):
    for i in range(4):
        p.fd(a)
        p.right(90)
    p.left(15)
turtle.done()