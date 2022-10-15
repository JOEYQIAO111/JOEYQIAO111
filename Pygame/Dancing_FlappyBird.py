import pygame
import random
import time 

pygame.init()
SCREEN = pygame.display.set_mode((300,500)) 
pygame.display.set_caption('Flappy Bird')
CLOCK = pygame.time.Clock()

bird = pygame.image.load('/Volumes/JOEYQIAO/School Mac/Python/Pygame/Flappy Bird 素材包/spritesyellow-up.png')

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            bird = pygame.transform.flip(bird,True,False)

            
    color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    SCREEN.fill(color)
    SCREEN.blit(bird,(150,250))
    pygame.display.update()
    CLOCK.tick(10)