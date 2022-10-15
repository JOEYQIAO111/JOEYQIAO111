#random circles
import turtle
import random
t = turtle.Pen()
t.speed(0)
def filled_circle(x,y,color):
        t.up()
        t.goto(x,y)
        t.down()
        t.color(color)
        t.begin_fill()
        t.circle(30)
        t.end_fill()
for i in range(100):
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    if x < 0:
        filled_circle(x,y,'red')
    else:
        filled_circle(x,y,'blue')
turtle.done()

'''# guessing numbers
import random
number = random.randint(0,100)
print('you have 8 tries')
for i in range(12):
    a = int(input('Guess a number between 0 and 100: '))
    if a == number:
        print('You got it!')
        break
    if a < number:
        print('Too small')
    if a > number:
        print('Too big')
if a != number:
    print('try again next time')   '''