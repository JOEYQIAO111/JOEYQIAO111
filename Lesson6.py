'''# Kite
import turtle
t = turtle.Pen()
def rhomb():
    for i in range(2):
        t.fd(100)
        t.right(60)
        t.fd(100)
        t.right(120)
    turtle.done()
rhomb()'''

# 4 kites
'''import turtle
t = turtle.Pen()
def rhomb():
    for i in range(2):
        t.fd(100)
        t.right(60)
        t.fd(100)
        t.right(120)
t.left(30)
for u in range(4):
    rhomb()
    t.right(90)
turtle.done()'''

'''# 12 pointed star
import turtle
t = turtle.Pen()
def rhomb():
    for i in range(2):
        t.fd(100)
        t.right(60)
        t.fd(100)
        t.right(120)
for u in range(6):
    rhomb()
    t.right(60)
t.left(30)
for  y in range(6):
    rhomb()
    t.right(60)
turtle.done()'''

'''# 12 pointed star with color
import turtle
t = turtle.Pen()
t.speed(0)
def rhomb():
    for i in range(2):
        t.fd(100)
        t.right(60)
        t.fd(100)
        t.right(120)
t.fillcolor('purple')
t.begin_fill()
for u in range(6):
    rhomb()
    t.right(60)
t.end_fill()
t.left(30)
t.fillcolor('yellow')
t.begin_fill()
t.pencolor('yellow')
for  y in range(6):
    rhomb()
    t.right(60)
t.end_fill()
turtle.done()
'''

'''#Don't study
print('I have a lot of homework')
u = input('Did I study? (yes/no)')
if u == 'yes':
    print('I pass the exam')
if u == 'no':
    print('I play')
print('I get happy')
print('I get tired')
print('I get sick')
print('I die')'''

# Username and Password
username = input('Enter username: ')
password = input('Enter password: ')
if username == 'JOEYQIAO111' and password == 'Vi0linist':
    print('Welcom back JOEYQIAO111')
if username != 'JOEYQIAO111' or password != 'Vi0linist':
    print ('wrong password or username')

'''# Odd or Even number
a = int(input('Enter a number(a%2 = 0/a%2 != 0): '))
if a%2 == 0:
    print('Even number')
if a%2 != 0:
    print('Odd number')'''

'''print('I am hungry')
a = input('Is mom at home: (yes/no)')
if a == 'yes':
    print('mom made dinner')
if a == 'no':
    s = input('would I make dinner for my self?: (yes/no)')
    if s == 'yes':
        print('I made dinner for my self')
    if s == 'no':
        print('I called delivery pizza')
print('I am full')'''