# This files contains the class and methods for the player object
import pygame

class player(pygame.sprite.Sprite):
    def __init__(self, spriteName, x=0, y=0):
        # Initiates position on the screen
        self.xpos = x
        self.ypos = y
        # Initiates the sprite of the player FROM THE ASSETS DIRECTORY
        self.setImage(pygame.image.load('assets/'+spriteName+'.png'))

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
