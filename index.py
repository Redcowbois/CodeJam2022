#Main File

###Setup###

import pygame
from sys import exit 
pygame.init()

from tiles import *

window = pygame.display.set_mode((1024, 576))
pygame.display.set_caption("CodeJam")
clock = pygame.time.Clock()
###


###Textures###

background = pygame.image.load("./assets/space.jpg").convert_alpha()
###


###Game Loop###
while True:
    window.blit(background, (0,0))

    generated_tiles = draw_tiles(window, display_map)
    for tile in generated_tiles:
        window.blit(tile.image, tile.rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)
###