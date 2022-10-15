import pgzrun
from pgzero.keyboard import keyboard, keys
from pgzero.actor import Actor

#定义窗口名称
TITLE = 'Studio365'

#定义窗口大小
WIDTH = 480
HEIGHT = 670

#定义飞机
plane = Actor('plane', (240, 600))
#定义背景图
bg = Actor('bg')     
#定义储存子弹的列表
bullets = []

#定义飞机的移动速度
plane.speed = 7

#画出图像
def draw():
    bg.draw()
    plane.draw()
    for i in bullets:
        i.draw()

#让飞机监测键盘然后前后左右移动
def player_move():
    #点wasd
    if keyboard.w and plane.y > 35:
        plane.y -= plane.speed
    if keyboard.a and plane.x > 20:
        plane.x -= plane.speed
    if keyboard.s and plane.y < 650:
        plane.y += plane.speed
    if keyboard.d and plane.x < 460:
        plane.x += plane.speed 
    
    #点方向键
    if keyboard.up and plane.y > 35:
        plane.y -= plane.speed
    if keyboard.left and plane.x > 20:
        plane.x -= plane.speed
    if keyboard.down and plane.y < 650:
        plane.y += plane.speed
    if keyboard.right and plane.x < 460:
        plane.x += plane.speed

#让子弹移动
def bullet_move():
    for i in bullets:
        i.y -= i.speed

#发射子弹
def on_key_down(key):
    bullet = Actor('bullet', (plane.x, plane.y))
    if key == keys.SPACE or key == keys.RSHIFT or key == keys.J:
        bullet.speed = 12
        bullets.append(bullet)

#更新画面
def update():
    player_move()
    bullet_move()

#运行程序
pgzrun.go()