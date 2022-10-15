import pgzrun
import random
from pgzhelper import Actor

#定义窗口
WIDTH = 500
HEIGHT = 700

#定义板块列表
blocks = []

#定义角色
player = Actor('player')
#让角色小一点
player.scale = 0.7
#让角色出现在屏幕中间
player.pos = WIDTH / 2, HEIGHT /2
#定义角色速度
player.speed = 5
#角色跳起来之前的高度
player.now_height = player.y
#定义角色不在跳
player.jump = False 

#定义block函数 创建板块
def bloc(image, x, y):
    #倒入板块
    block = Actor(image)

    #定义板块坐标
    block.x = x
    block.y = y

    #定义板块大小
    block.scale = 0.7
    #定义板块向下移动速度
    block.speed = 5

    #返回block
    return block

#调用bloc函数
for i in range(20):
    #让板块的坐标随机生成
    x = random.randint(10, WIDTH - 10)
    y = (i + 1) * random.randint(35, 40)
    #传参数
    block = bloc('green', x, y)
    #添加板块
    blocks.append(block)

#画出东西
def draw():
    #设定背景为白色
    screen.fill((255, 255, 255))
    #画出板块
    for block in blocks:
        block.draw()
    #画出角色
    player.draw()

def update():
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

    #让角色往上跳
    if player.jump:
        player.y -= player.speed
        if player.y <= HEIGHT * 1 / 2:
            for block in blocks:
                block.y += block.speed
                if block.y > HEIGHT:
                    blocks.remove(block)
                    new_block = bloc('green', random.randint(10, WIDTH - 10), 0)
                    blocks.append(new_block)
                        
        if player.y <= player.now_height - 200:    
            player.jump = False

    #让角色才到板块后往上跳
    else:
        player.y += player.speed
        for block in blocks:
            if player.right > block.left and player.left < block.right and abs(block.top - player.bottom) < 5:
                player.now_height = player.y
                player.jump = True

#运行程序
pgzrun.go()