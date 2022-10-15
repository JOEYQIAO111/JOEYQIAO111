import pgzrun
from pgzhelper import Actor
import random

#定义窗口大小
WIDTH = 500
HEIGHT = 700

#定义角色
player = Actor('player')

#定义板块
block = Actor('green')

#储存板块
block_list = []

#定义板块
for i in range(20):
    #定义板块
    block = Actor('green')
    #让板块小点
    block.scale = 0.7
    #让板块的坐标随机生成
    block.x = random.randint(10, WIDTH - 10)
    block.y = (i + 1) * random.randint(35, 40)
    block_list.append(block)

#让角色变小点
player.scale = 0.7

#定义角色移动速度
player.speed = 5

#定义角色的位置
player.x = WIDTH / 2
player.y = HEIGHT

#定义角色状态
#status: 1:right, 2:left, 3:up, 4:down, 5:dead
player.status = 3

height1 = player.y

#画出东西
def draw():
    #画出窗口，背景为白色
    screen.fill((255,255,255))
    #画出角色
    player.draw()

    #画出板块
    for block in block_list:
        block.draw()

    #如果玩家死了就显示Game Over
    if player.status == 5:
        screen.draw.text('Game Over', (WIDTH / 2 - 150, HEIGHT / 2),
                        fontsize = 50, fontname = 's', color = 'red'
        )

#让画出的东西动
def update():

    #让height1能在update函数利里用
    global height1

    #当按下左键，角色面向左边往左走
    if keyboard[keys.LEFT]:
        #让角色换图片
        player.image = 'player'
        #让角色往左走
        player.x -= player.speed
        #当角色超出屏幕让他从另一边回来
        if player.x <= 0:
            player.x = WIDTH

    #当按下右键，角色面向右边往右走
    if keyboard[keys.RIGHT]:
        #让角色换图片
        player.image = 'player1'
        #让角色往右走
        player.x += player.speed
        #当角色超出屏幕让他从另一边回来
        if player.x >= WIDTH:
            player.x = 0

    #如果玩家是往上的
    if player.status == 3:
        #-y轴让角色以 5 * 1.5的速度往上
        player.y -= player.speed * 1.5
        #如果到屏幕的中间就往下掉
        if player.y <= height1 - 300:
            #就往下掉
            player.status = 4

    #如果玩家在往下
    elif player.status == 4:
        #让角色往下
        player.y += player.speed

        #让角色往上走
        for block in block_list:
            if player.right > block.left + 5 and block.left < block.right - 5 and abs(block.top - player.bottom) < 3:
                player.status = 3
                height1 = player.y

        #如果玩家掉到地上
        if player.y > HEIGHT:

            height1 = player.y
            #角色死了
            player.status = 3

#运行程序
pgzrun.go()