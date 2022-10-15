import pgzrun
import random
from pgzhelper import Actor as A

#定义窗口大小
WIDTH = 600
HEIGHT = 800

#砖块的速度
brick_speed = 2

#储存砖块
bricks = []

score = 0

#for循环创建5个砖块
for i in range(5):
    
    #导入砖块图片并定义为brick
    brick = A('brick')

    #定义砖块随机坐标
    brick.pos = random.randint(0,600), 150 * (i+1)

    #把5块砖块加入bricks列表
    bricks.append(brick)

#定义角色
Doge = A('doge')

#定义角色位置
Doge.x = WIDTH / 2
Doge.y = HEIGHT / 5

#定义角色大小
Doge.scale = 0.8

#定义角色移动速度
Doge.speed = 5

#角色最新的y坐标
updated_player_y = Doge.y

#定义游戏没有结束
close = False

#定义draw函数画出角色
def draw():

    #清空屏幕
    screen.clear()

    #画出角色
    Doge.draw()

    scores = screen.draw.text(f'Score = {score}', (0,0),
                        fontsize = 25, fontname = 's', color = 'red')


    #失败后，显示Game Over
    if close:
        screen.draw.text('Game Over', (30, HEIGHT / 2-100),
                        fontsize = 100, fontname = 's', color = 'red')

    #画出砖块
    for brick in bricks:
        brick.draw()

#定义update函数移动角色
def update():

    #让这些变量能在函数里被使用
    global close, brick_speed, updated_player_y, score

    #设定角色不在砖块上
    is_player_on_brick = False

    #循环bricks
    for brick in bricks:

        #判断角色是否在砖块上
        if Doge.right > brick.left and Doge.left < brick.right and abs(brick.top - Doge.bottom) < 5:

            #把狗头的角度调正
            Doge.angle = 0

            #设定玩家在砖块上
            is_player_on_brick = True
            
            #让角色跟砖块同时朝上移动
            Doge.bottom = brick.top
            
            #更新角色位置
            updated_player_y = Doge.y

    #让角色往下掉
    if not is_player_on_brick:
        Doge.angle += 45
        Doge.y += 3

    #移动每一块砖块
    for brick in bricks:
        brick.y -= brick_speed

    #把到达屏幕顶部上的砖块删掉并从下面出现新的砖块
    if bricks[0].top < 10:
        del bricks[0]
        brick = A('brick')
        brick.x = random.randint(100,500)
        brick.y = HEIGHT
        bricks.append(brick)
        score += 1

    if not close: 
        #监听左键让角色朝左移动（减x坐标）
        if keyboard.left:
            Doge.x -= Doge.speed

        #监听右键让角色朝右移动（加x坐标）
        if keyboard.right:
            Doge.x += Doge.speed

    #如果Doge的头顶除了屏幕或下面出了屏幕就结束游戏
    if Doge.top < 0 or Doge.bottom > HEIGHT:
        close = True
        Doge.speed = 0
        brick_speed = 0

#运行程序
pgzrun.go()