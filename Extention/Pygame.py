'''import pygame
import sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600,500)) 
my_font =  pygame.font.Font(None,60)
white = 255,255,255 
blue = 0,0,255
textImage = my_font.render('Hello pygame',True,white ) 
while True: 
    for event in pygame.event.get(): 
        if event.type in (QUIT,KEYDOWN):
            sys.exit()
    screen.fill(blue)
    screen.blit(textImage,(100,100))
    pygame.display.update() '''

import pygame
import sys
from pygame.locals import *
pygame.init()
white = 255,255,255
blue = 0,0,200
screen = pygame.display.set_mode((600,500))
pygame.display.set_captions('draw a circle')
while True:
    for event in pygame.event.get():
        if event.type in (QUIT,KEYDOWN):
            sys.exit()
        screen.fill(blue)