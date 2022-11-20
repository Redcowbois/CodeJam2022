# This files contains the class and methods for the player object
import pygame
import numpy as np

class player(pygame.sprite.Sprite):
    def __init__(self, spriteName, x=0, y=0):
        super().__init__()
        # Initiates position on the screen
        self.falling = True
        self.hitting_left = False
        self.hitting_right = False
        self.xpos = x
        self.ypos = y
        self.sprite_name = spriteName
        # Initiates the sprite of the player FROM THE ASSETS DIRECTORY
        self.image = pygame.image.load('assets/'+self.sprite_name+'.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = (0, 0))

        self.velocity = np.array([0,0])
        self.acceleration = np.array([0,1])

    def setImage(self, sprite):
        # Sets the sprite of the player and gets its size
        self.image = sprite
        self.rect = self.image.get_rect(bottomleft = (self.xpos, self.ypos))
        self.size = self.image.get_size()

    def scale(self, width, height):
        # Scales the sprite of the player to given width and height values
        self.setImage(pygame.transform.scale(self.image, (width, height)))

    def setPos(self, x, y):
        # Sets the position of the player
        self.xpos = x
        self.ypos = y

    def getImage(self):
        # Returns player sprite
        return self.image

    def getPos(self):
        # Returns player position in a tuple
        return (self.xpos, self.ypos)
    
    def update_Movement(self):
        #moves the player around
        if pygame.key.get_pressed()[pygame.K_a]:
            # Goes left
            self.velocity[0] = -4

        elif pygame.key.get_pressed()[pygame.K_d]:
            # Goes right
            self.velocity[0] = 4
        else:
            # Does not move
            self.velocity[0] = 0
        if pygame.key.get_pressed()[pygame.K_SPACE] and not self.falling:
            self.velocity[1] = -20
            self.falling = True

        if self.falling:
            self.velocity[1] += 1
        elif not self.falling:
            self.velocity[1] = 0

        self.xpos += self.velocity[0]
        self.ypos += self.velocity[1]
