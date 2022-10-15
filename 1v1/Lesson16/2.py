import pygame
import sys

#初始化*
pygame.init()

#定义窗口大小
size = width, height = 1600, 800

#创建窗口
window = pygame.display.set_mode(size)

pos = 100,100
W = (255, 255, 255)
B = (0, 0, 0)

#给窗口填充颜色、
window.fill((250, 250, 250))

while True:
    for event in pygame.event.get():
        #让程序关闭*
        if event.type == pygame.QUIT:
            sys.exit()
    
    pygame.draw.rect(window,B,(50,50,100,50),1) # 0填充
    # 多边形
    pygame.draw.polygon(window,B,[(200,200),(100,300),(300,300)],1)
    # 圆形
    pygame.draw.circle(window,B,pos,75,1)
    # 椭圆形
    pygame.draw.ellipse(window,B,(100,100,400,100),1)
    
    #让窗口里的东西可以动
    pygame.display.flip()