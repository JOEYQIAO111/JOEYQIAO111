'''# half rainbow circle
import turtle
turtle.tracer(False)
turtle.colormode(255)
b = 255
a = 2
d = 1
for i in range(256):
    if a > 253:
        d = d + 2
        a = 255
        b = 255-d
    if d > 255:
        break
    turtle.color(b,a,0)
    a = a + 2
    turtle.dot(255-i)
turtle.done()'''

#full rain bow circle
import turtle
turtle.colormode(255)
turtle.tracer(False)
R = 255
G = 1
B = 1
c = 1
for i in range(765):
    if G > 255:
        c = c + 2
        G = 255
        R = 255-c
    if c > 255:
        R = 0
        B = B + 2
    if B > 253:
        B = 255
        G = G - 2
    turtle.color(R,G,B)
    G = G + 2
    turtle.dot(765-i)
turtle.done()