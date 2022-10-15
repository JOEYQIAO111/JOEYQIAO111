# all number's sum between 1-100
'''a = 0
b = 1
while b <= 100:
    a = a + b
    b = b + 1
print(a)'''

#Notes
'''for i in range(10):
    print(i, end=' ')
print()

for i in range(0,10):
    print(i, end=' ')
print()

for i in range(0,10,3):
    print(i, end=' ')
print()'''

'''a = 'qwer'
for i in a:
    print(i)'''

'''a = 'qwer'
for i in range(len(a)):
    print(a[i])'''

'''a = input('Enter numbers or letter randomly: ')
for i in a:
    if i in '0123456789':
        print(i,end=' ')'''

'''import turtle
t = turtle.Pen()
t.speed(0)
turtle.colormode(255)
for i in range(256):
    t.color(255,i,0)
    t.dot(i)
turtle.done()'''

#color circle
'''import turtle
turtle.speed(0)
turtle.colormode(255)
for i in range(256):
    turtle.color(0,255,255-i)
    turtle.dot(255-i)
turtle.done()'''