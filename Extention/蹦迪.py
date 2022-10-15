import pygame
import random
import time 

pygame.init()
SCREEN = pygame.display.set_mode((2560, 1280)) 
pygame.display.set_caption('蹦迪')
CLOCK = pygame.time.Clock()

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    SCREEN.fill(color)
    pygame.display.update()
    CLOCK.tick(10)