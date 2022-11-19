import pygame

class FloorTile(pygame.sprite.Sprite):              #Class for floor tiles
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load("./assets/floor.png").convert_alpha()
        self.rect = self.image.get_rect(bottomleft = (pos_x, pos_y))
        self.id = "10"                                #Id here is 10 so we can easily have sub id #11, #12...


display_map = [[],[],[],[],[],
                [],[],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],[]]

def draw_tiles(window, display_map):
    """
    Draws the tiles, takes the window its gonna draw it to and the 
    display map as inputs. Returns nothing.
    """
    generated_tiles = []

    for row in range(len(display_map)):
        if len(display_map[row]) == 0: #Skips an iteration if there is nothing in the row
            continue

        for col in range(len(display_map[row])):
            if display_map[row][col] == 10:
                generated_tiles.append(FloorTile(col*64, row*64))
    
    return generated_tiles

