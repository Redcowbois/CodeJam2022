#Main File
skip_menu = False #SET TO TRUE TO SKIP MENU
###Setup###

import pygame
from sys import exit 
pygame.init()

from tiles import *
from player import *

window = pygame.display.set_mode((1024, 576))
pygame.display.set_caption("CodeJam")
clock = pygame.time.Clock()
pygame.mixer.init(48000, -16, 1, 1024)
###


###Textures and Sounds###

background = pygame.image.load("./assets/menu.png").convert_alpha()         #initialization of assets

red_amongus = pygame.image.load("./assets/menu_amongus.png")
red_amongus.set_colorkey("white")
red_amongus = red_amongus.convert_alpha()
red_amongus_rect = red_amongus.get_rect(topleft = (400, 250))

red_amongus_sus = pygame.image.load("./assets/menu_sus.png")
red_amongus_sus.set_colorkey("white")
red_amongus_sus = red_amongus_sus.convert_alpha()
red_amongus_sus_rect = red_amongus_sus.get_rect(topleft = (420, 250))

sus_sound = pygame.mixer.Sound('./assets/audio/sus_sound.mp3')
###


###Main Menu Loop###

while not skip_menu:
    window.blit(background, (0,0))

    if red_amongus_rect.collidepoint(pygame.mouse.get_pos()):
        window.blit(red_amongus_sus, red_amongus_rect)
        if pygame.mouse.get_pressed()[0]:
            sus_sound.play()
            break
    else: 
        window.blit(red_amongus, red_amongus_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)
###

###Game Loop###
amogus = player("amogus0")
amogus.scale(64,64)
player_group = pygame.sprite.GroupSingle() #Group Class for player, makes interacting with tiles easier
player_group.add(amogus)

time_since_start = pygame.time.get_ticks()       #Music
background = pygame.image.load("./assets/space.jpg").convert_alpha()
sus_sound = pygame.mixer.Sound('./assets/audio/sussy_music.mp3')
sus_sound.set_volume(0.05)

v = 0 
current_time = pygame.time.get_ticks()

while True:
    window.blit(background, (0,0)) #Draw background (always first)
    tile_group = draw_tiles(display_map)
    tile_group.draw(window)

    
    print(len(pygame.sprite.groupcollide(player_group, tile_group, False, False)))
    if len(pygame.sprite.groupcollide(player_group, tile_group, False, False)) == 0:
        amogus.ypos += 2

    amogus.update_Movement()
    amogus.rect.update(amogus.xpos, amogus.ypos, 64, 64)
    
    dt = pygame.time.get_ticks() - current_time
        
    # collision = pygame.sprite.spritecollide(amogus, tile_group, True)
    # print(collision)


    window.blit(amogus.getImage(), amogus.getPos())
    
    if pygame.time.get_ticks() >= time_since_start+4000: #Plays music after a delay
        sus_sound.play(-1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.update()
    clock.tick(60)
    current_time = pygame.time.get_ticks()
###