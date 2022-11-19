# This files contains the class and methods for the player object
import pygame

class player1:
    def __init__(self, spriteName, x=0, y=0):
        # Initiates position on the screen
        self.xpos = x
        self.ypos = y
        # Initiates the sprite of the player FROM THE ASSETS DIRECTORY
        self.setSprite(pygame.image.load('assets/'+spriteName+'.png'))

    def setSprite(self, sprite):
        # Sets the sprite of the player and gets its size
        self.sprite = sprite
        self.size = self.sprite.get_size()

    def scale(self, width, height):
        # Scales the sprite of the player to given width and height values
        self.setSprite(pygame.transform.scale(self.sprite, (width, height)))

    def setPos(self, x, y):
        # Sets the position of the player
        self.xpos = x
        self.ypos = y

    def getSprite(self):
        # Returns player sprite
        return self.sprite

    def getPos(self):
        # Returns player position in a tuple
        return (self.xpos, self.ypos)
