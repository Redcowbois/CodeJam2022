#Main File

###Setup###

import pygame
from sys import exit 
pygame.init()

from tiles import *
from player import *

window = pygame.display.set_mode((1024, 576))
pygame.display.set_caption("CodeJam")
clock = pygame.time.Clock()
###


###Textures###

background = pygame.image.load("./assets/space.jpg").convert_alpha()
###


###Game Loop###
amogus = player("amogus")
amogus.scale(150,150)
while True:
    window.blit(background, (0,0))

    generated_tiles = draw_tiles(window, display_map)
    for tile in generated_tiles:
        window.blit(tile.image, tile.rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    window.blit(amogus.getImage(), amogus.getPos())

    pygame.display.update()
    clock.tick(60)
###