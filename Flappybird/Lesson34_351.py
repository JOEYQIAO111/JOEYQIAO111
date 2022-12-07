import pgzrun
from pgzhelper import Actor
import random

#定义窗口名字
TITLE = 'Flappy Bird'

#定义窗口大小
WIDTH = 400
HEIGHT = 708

#定义小鸟角色
bird = Actor('bird0', (75, 200))
#让小鸟大一点
bird.scale = 1.3
#定义小鸟是活着的
bird_dead = False
#定义小鸟往下的重力
bird.vy = 0  
#定义分数
bird.score = 0
#定义最高分数
bird.high = 0

#定义管子中间缺口的高度
GAP = 130
#定义管子移动的速度
SPEED = 3 
#定义重力
GRAVITY = 0.35
#定义每次往上的距离
FLAP_STRENGTH = 6

def on_key_down(key):
    #如果小鸟还活着
    if not bird_dead:
        #判断如果按下空格
        if key == keys.SPACE:
            #让小鸟往上走
            bird.vy = -FLAP_STRENGTH

#定义管子随机生成的位置
def pipe_pos():
    #定义管子中间空隙的中间的随机坐标
    pipe_gap_y = random.randint(200, HEIGHT - 200)
    #根据pipe_gap_y定义上面的管子的坐标
    pipe_top.pos = (WIDTH, pipe_gap_y - GAP/2)
    #根据pipe_gap_y定义下面的管子的坐标
    pipe_bottom.pos = (WIDTH, pipe_gap_y + GAP/2)

#定义管子的点是在底部和顶部
pipe_top = Actor('top', anchor = ('middle', 'bottom'))
pipe_bottom = Actor('bottom', anchor = ('middle', 'top'))

#调用函数
pipe_pos()

#让管子移动
def pipe_update():
    #让管子往左走
    pipe_top.x -= SPEED
    pipe_bottom.x -= SPEED

    #如果管子超出屏幕就重新画一个
    if pipe_top.right < 0:
        pipe_pos()
        if not bird_dead:
            bird.score += 1

#更新小鸟
def bird_update():
    #让bird_dead能在函数里用
    global bird_dead    

    #让小鸟模拟重力往下
    bird.vy += GRAVITY
    #让小鸟的位置跟bird.vy同步
    bird.y += bird.vy
    #让小鸟的位置呆在同一个位置
    bird.x = 75

    if not bird_dead:
        #换成活着的小鸟的图片
        bird.image = 'bird1'
    
    #判断小鸟有没有撞到管子
    if bird.colliderect(pipe_top) or bird.colliderect(pipe_bottom):
        #如果碰到了就定义小鸟死了 
        bird_dead = True
        #换成死掉的小鸟的图片
        bird.image = 'birddead'
    
    if not 0 < bird.y < 720:
        #判断最高分
        if bird.score > bird.high:
            bird.high = bird.score
        #定义鸟死了
        bird_dead = True
        #换成活着的小鸟的图片
        bird.image = 'bird0'
        #让小鸟回到出生点
        bird.y = 200
        #让小鸟复活
        bird_dead = False
        #清零分数
        bird.score = 0
        #还原小鸟下降的速度
        bird.vy = 0


#画出东西
def draw():
    #画出背景图
    screen.blit('background',(0,0))
    #画出上面的管子
    pipe_top.draw()
    #画出下面的管子
    pipe_bottom.draw()
    #画出小鸟
    bird.draw()
    #画出分数
    screen.draw.text(
        f'{bird.score}/{bird.high}',
        color = 'white',
        midtop = (WIDTH // 2, 10),
        fontsize = 70,
        shadow = (1,1)
    )
    
def update():
    #调用pipe_update函数
    pipe_update()
    #调用bird_update函数
    bird_update()

#运行程序
pgzrun.go()