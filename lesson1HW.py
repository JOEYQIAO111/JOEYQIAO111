'''# 4 pointed star
import turtle
p = turtle.Pen()
p.color('yellow')
p.left(60)
for i in range(4):
    p.forward(100)
    p.right(160)
    p.forward(100)
    p.left(70)
turtle.done()'''

# normal star
import turtle
s = turtle.Pen()
s.color("yellow")
s.fillcolor("yellow")
s.begin_fill()
s.left(70)
for i in range(5):
    s.forward(100)
    s.right(140)
    s.forward(100)
    s.left(68)
s.end_fill()
turtle.done()