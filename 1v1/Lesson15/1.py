import pygame
import sys

#初始化*
pygame.init()

#定义窗口大小
size = width, height = 800, 600

#创建窗口
window = pygame.display.set_mode(size)

#给窗口填充颜色、
window.fill((5,234,163))

#导入gui图
turtle = pygame.image.load('1v1/Lesson15/gui.png')
#让gui改变大小
turtle_scale = pygame.transform.scale(turtle, (100,100))
#gui的位置
turtle_pos = turtle_scale.get_rect()

#定义速度
turtle_sped = [0, 0]

#让gui转头
LH = turtle_scale
RH = pygame.transform.flip(turtle_scale, True, False)

while True:
    for event in pygame.event.get():
        #让程序关闭*
        if event.type == pygame.QUIT:
            sys.exit()
        
        #让gui上线左右动 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                turtle_scale = LH
                turtle_sped = [-1,0]
            if event.key == pygame.K_d:
                turtle_scale = RH
                turtle_sped = [1,0]
            if event.key == pygame.K_w:
                turtle_sped = [0,-1]
            if event.key == pygame.K_s:
                turtle_sped = [0,1]

    #让gui撞墙反弹
    if turtle_pos.left < 0 or turtle_pos.right > width:
        turtle_scale = pygame.transform.flip(turtle_scale, True, False)  
        turtle_sped[0] = -turtle_sped[0]
    if turtle_pos.top < 0 or turtle_pos.bottom > height: # 反向移动
        turtle_sped[1] = -turtle_sped[1]

    #让gui动
    turtle_pos = turtle_pos.move(turtle_sped)

    #给窗口填充颜色、
    window.fill((5,234,163))

    #画图片
    window.blit(turtle_scale, turtle_pos)

    #让窗口里的东西可以动
    pygame.display.flip()

    #延迟三毫秒
    pygame.time.delay(3)