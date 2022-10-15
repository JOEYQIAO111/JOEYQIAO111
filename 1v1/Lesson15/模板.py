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

while True:
    for event in pygame.event.get():
        #让程序关闭*
        if event.type == pygame.QUIT:
            sys.exit()
    
    #让窗口里的东西可以动
    pygame.display.flip()