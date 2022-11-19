#Main File

import pygame
from sys import exit 
pygame.init()

window = pygame.display.set_mode((100, 562))
pygame.display.set_caption("CodeJam")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)

