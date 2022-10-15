#list
#max min sum sort append insert index count len remove pop

'''
现有一个列表li = [1,2,3,'a',4,'c'],
有一个字典dic={}
如今须要完成这样的操做：
1.循环输入五个k1
2.若是该字典没有"k1"这个键，那就建立这个"k1"键和对应的值(该键对应的值为空列表)k1: []
并将列表li中的索引位为奇数对应的元素,添加到"k1"这个键对应的空列表中。
3.若是该字典中有"k1"这个键。那就将该列表li中的索引位为奇数对应的元素
添加到"k1"，这个键对应的值中。
'''

'''li = [1, 2, 3, 'a', 4, 'C']
dic = {}
for i in range (5):
    k1 = input("请输入k1:")
if k1 not in dic:
    dic[k1] = []
else:
    for i in range(len(li)):
        if i % 2 != 0:
            dic[k1].append(li[i])
print(dic)'''

'''
import pgzrun
import random

balls = []

# 800 * 600
def draw():
    screen.fill((255, 255, 255))
    for ball in balls:
        screen.draw.filled_circle((ball[0], ball[1]), ball[4], ball[5])

def update():
    for ball in balls:
        ball[0] += ball[2]
        ball[1] += ball[3]

        if ball[1] > 570 or ball[1] < 30:
            ball[3] = -1 * ball[3]

        if ball[0] > 770 or ball[0] < 30:
            ball[2] = -1 * ball[2]

def on_mouse_move(pos):
    x = pos[0]
    y = pos[1]
    speed_x = random.randint(-5, 5)
    speed_y = random.randint(-5, 5)
    r = random.randint(-5, 30)
    color = (random.randint(0,255), random.randint(0,255),random.randint(0,255))
    ball = [x, y, speed_x, speed_y, r, color]
    balls.append(ball)

pgzrun.go()
'''

import pgzero
import random

ball = []

#800 * 600
def draw():
    screen.fill(r, g, b)

def update():
    pass

def mouse(pos):
    x = pos[0]