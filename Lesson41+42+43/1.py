import pgzrun
import random
from pgzero.actor import Actor

#定义窗口的名称和大小
TITLE = 'Studio365'
WIDTH, HEIGHT = 300, 300

#定义装图片的列表
pics = []

#定义图片
imgs = ['3脳3_01', '3脳3_02', '3脳3_03', '3脳3_04', '3脳3_05','3脳3_06', '3脳3_07',
        '3脳3_08','3脳3_09']

victory = False

#导入图片并添加到列表
for i in range(3):
    for u in range(3):
        pic1 = Actor(imgs[i*3+u], (u * 100 + 50, i * 100 + 50))
        pics.append(pic1)

#改变图片的位置
def swapPosition(i,u):
    pics[i].pos, pics[u].pos = pics[u].pos, pics[i].pos

#随机图片的位置
for i in range(10):
    n = random.randint(0,8)
    m = random.randint(0,8)
    swapPosition(n,m)

#画出图片
def draw():
    screen.clear()
    for i in pics:
        i.draw()
    
    if victory:
        screen.draw.text(
            'victory',
            color = 'black',
            fontsize = 80,
            midtop = (WIDTH // 2, 120)
        )
    
    else:
        screen.draw.line((0,100), (300,100), color='green')
        screen.draw.line((0,200), (300,200), color='green')
        screen.draw.line((100,0), (100,300), color='green')
        screen.draw.line((200,0), (200,300), color='green')
    
        if click1 != -1:
            screen.draw.rect(Rect((pics[click1].left, pics[click1].top), (100,100)), color='red')

#点击检测
clickall = 0
click1 = click2 = -1

#让玩家改变图片位置
def on_mouse_down(pos, button):
    global clickall, click1, click2, victory
    #查找点的是那张图片 
    for i in range(9):
        if pics[i].collidepoint(pos):
            break

    clickall += 1

    if clickall % 2 != 0:
        click1 = i

    else:
        click2 = i
        swapPosition(click1, click2)
    
    victory = True
    for i in range(3):
        for u in range(3):
            t = pics[i*3+u]
            if t.pos != (u * 100 + 50, i * 100 + 50):
                victory = False
                break

    print(victory)


#运行程序
pgzrun.go()
