import pygame
import random
import os
import time 

W, H = 288,512
FPS =  30

pygame.init()
SCREEN = pygame.display.set_mode((285,500))  
pygame.display.set_caption('Flappy Bird')
CLOCK = pygame.time.Clock()

ybirdup = pygame.image.load('/Volumes/JOEYQIAO/School Mac/Python/Pygame/Flappy Bird 素材包/sprites/yellow-up.png')
ybirdmid = pygame.image.load('/Volumes/JOEYQIAO/School Mac/Python/Pygame/Flappy Bird 素材包/sprites/yellow-mid.png')
ybirddown = pygame.image.load('/Volumes/JOEYQIAO/School Mac/Python/Pygame/Flappy Bird 素材包/sprites/yellow-down.png')

bbirdup = pygame.image.load('/Volumes/JOEYQIAO/School Mac/Python/Pygame/Flappy Bird 素材包/sprites/blue-up.png')
bbirdmid = pygame.image.load('/Volumes/JOEYQIAO/School Mac/Python/Pygame/Flappy Bird 素材包/sprites/blue-mid.png')
bbirddown = pygame.image.load('/Volumes/JOEYQIAO/School Mac/Python/Pygame/Flappy Bird 素材包/sprites/blue-down.png')

rbirdup = pygame.image.load('/Volumes/JOEYQIAO/School Mac/Python/Pygame/Flappy Bird 素材包/sprites/red-up.png')
rbirdmid = pygame.image.load('/Volumes/JOEYQIAO/School Mac/Python/Pygame/Flappy Bird 素材包/sprites/red-mid.png')
rbirddown = pygame.image.load('/Volumes/JOEYQIAO/School Mac/Python/Pygame/Flappy Bird 素材包/sprites/red-down.png')

bgpic = pygame.image.load('/Volumes/JOEYQIAO/School Mac/Python/Pygame/Flappy Bird 素材包/sprites/day.png')
guide = pygame.image.load('/Volumes/JOEYQIAO/School Mac/Python/Pygame/Flappy Bird 素材包/sprites/guide.png')
floor = pygame.image.load('/Volumes/JOEYQIAO/School Mac/Python/Pygame/Flappy Bird 素材包/sprites/floor.png')
gpipe = pygame.image.load('/Volumes/JOEYQIAO/School Mac/Python/Pygame/Flappy Bird 素材包/sprites/green-pipe.png')
rpipe = pygame.image.load('/Volumes/JOEYQIAO/School Mac/Python/Pygame/Flappy Bird 素材包/sprites/red-pipe.png')
gameover = pygame.image.load('/Volumes/JOEYQIAO/School Mac/Python/Pygame/Flappy Bird 素材包/sprites/gameover.png')

'''IMAGES =  {}
for image in os.listdir('/Volumes/JOEYQIAO/School Mac/Python/Pygame/Flappy Bird 素材包/sprites'):
    name,extention = os.path.splitext(image)
    path = os.path.join('/Volumes/JOEYQIAO/School Mac/Python/Pygame/Flappy Bird 素材包/sprites',  image)
    IMAGES[name] = pygame.image.load(path)'''

floor_y = H - ybirdmid.get_height()
start = pygame.mixer.Sound('/Volumes/JOEYQIAO/School Mac/Python/Pygame/Flappy Bird 素材包/audio/start.wav')
die = pygame.mixer.Sound('/Volumes/JOEYQIAO/School Mac/Python/Pygame/Flappy Bird 素材包/audio/die.wav')
hit = pygame.mixer.Sound('/Volumes/JOEYQIAO/School Mac/Python/Pygame/Flappy Bird 素材包/audio/hit.wav') 
score = pygame.mixer.Sound('/Volumes/JOEYQIAO/School Mac/Python/Pygame/Flappy Bird 素材包/audio/score.wav')
flap = pygame.mixer.Sound('/Volumes/JOEYQIAO/School Mac/Python/Pygame/Flappy Bird 素材包/audio/flap.wav')

def main():
    while True: 
        start.play()
        menu_window()
        game_window()
        end_window()

def menu_window():
    guide_x = (W - guide.get_width())/2 
    guide_y = (floor_y - guide.get_height())/2 
    bird_x = W * 0.2 
    bird_y = (H - ybirdmid.get_height())/2
     
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return
        SCREEN.blit(bgpic,(0,0))
        SCREEN.blit(floor,(0,floor_y))
        SCREEN.blit(guide,(guide_x,guide_y))
        SCREEN.blit(ybirdmid,(bird_x, bird_y))
        
        pygame.display.update()
        CLOCK.tick(FPS)

def game_window():
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return
        SCREEN.blit(bgpic,(0,0))
        SCREEN.blit(floor,(0,floor_y))
        SCREEN.blit(ybirdmid,(W/2, H*0.3))
        pygame.display.update()
        CLOCK.tick(FPS)

def end_window():
    gameover_x = (W - gameover.get_width())/2
    gameover_y = (floor_y - gameover.get_height())/2
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return
        SCREEN.blit(gameover,(gameover_x,gameover_y))
        SCREEN.blit(floor,(0,floor_y))
        pygame.display.update()
        CLOCK.tick(FPS)

main()