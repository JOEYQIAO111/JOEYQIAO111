import pygame, sys

pygame.init()
size = width, height =  800, 400
window = pygame.display.set_mode(size)
pygame.display.set_caption('文件自动下载')
font1 = pygame.font.Font('Monaco.ttf', 30)
clock = pygame.time.Clock()
num = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    num += 1

    pygame.draw.rect(window, (127.5, 127.5,127.5),(150, 150, 500, 40))
    pygame.draw.rect(window, (5,234,163), (150, 150, num % 500, 40))
    
    text1 = font1.render(f'{int(num%500/500*100)}%', True, (255,255,255))
    window.blit(text1, (380,155))

    clock.tick(120)
    pygame.display.flip()