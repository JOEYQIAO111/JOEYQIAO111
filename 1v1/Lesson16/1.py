import pygame
import sys

#初始化*
pygame.init()

#定义窗口大小
size = width, height = 1200, 600

#创建窗口
window = pygame.display.set_mode(size)

#给窗口填充颜色、
window.fill((0, 0, 0))

#定义字体
font1 = pygame.font.Font('Monaco.ttf', 50)

#定义文字
text1 = font1.render("what is up -> what's up -> sup", True, (5,234,163))

window.blit(text1, (60,100))

while True:
    for event in pygame.event.get():
        #让程序关闭*
        if event.type == pygame.QUIT:
            sys.exit()
    
    #让窗口里的东西可以动
    pygame.display.flip()