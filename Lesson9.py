# random circles with lables
'''import turtle
import random
t = turtle.Pen()
t.speed(0)
number = 0
def circles(number):
    while number < 10:
        number = number + 1
        x = random.randint(-200,200)
        y = random.randint(-200,200)
        t.up()
        t.goto(x,y)
        t.down()
        t.circle(50)
        t.write(number, font = ('',30,''))
    turtle.done()   
circles(number)'''

# random circles with lables with the last number red
import turtle
import random
number = int(input('Enter the number of circles you want: '))
def circles(number):
    while True:
        if number == 0:
            t.pencolor('red')
            x = random.randint(-200,200)
            y = random.randint(-200,200)
            t.up()
            t.goto(x,y)
            t.down()
            t.circle(50)
            t.write(number, font = ('',30,''))
            break
        x = random.randint(-200,200)
        y = random.randint(-200,200)
        t.up()
        t.goto(x,y)
        t.down()
        t.circle(50)
        t.write(number, font = ('',30,''))
        number = number - 1
    turtle.done()
t = turtle.Pen()
t.speed(0)
circles(number)

'''import random
while True:
    a = random.randint(0,100)
    if a % 2 == 0:
        continue
    print(a)'''