import pygame
import sys

pygame.init()

size = width, height = 1700, 900

window = pygame.display.set_mode(size)

font = pygame.font.Font('Monaco.ttf', 20)

lineheight = font.get_linesize()

po = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        text =  font.render(str(event), True, (0, 255, 0))
        window.blit(text,(100, po))
        po += lineheight

        if po > height:
            po = 0
            window.fill((0, 0,  0))

        pygame.display.flip()