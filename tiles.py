import pygame

class FloorTile(pygame.sprite.Sprite):              #Class for floor tiles
    def __init__(self, pos_x, pos_y, is_large):
        super().__init__()

        if is_large:
            self.id = "11" #2x2 of 32 pixel tile
        else: 
            self.id = "10" #1x1 of 32 pixel tile
        
        self.image = pygame.image.load("./assets/floor.png").convert_alpha()
        self.rect = self.image.get_rect(bottomleft = (pos_x, pos_y))

display_map = [[],[],[],[],[],[],[],
    [],[11,11,11,11,0,0,0,0,0,11,11,11,11,11,11,11],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]]

def draw_tiles(display_map):
    """
    Draws the tiles, takes the window its gonna draw it to and the 
    display map as inputs. Returns nothing.
    """
    tile_group = pygame.sprite.Group()

    for row in range(len(display_map)):
        if len(display_map[row]) == 0: #Skips an iteration if there is nothing in the row
            continue

        for col in range(len(display_map[row])):
            if display_map[row][col] == 10: #Regular Tile
                tile_group.add(FloorTile(col*64, row*64, False))
                tile_group.add(FloorTile(col*64+32, row*64, False))

            if display_map[row][col] == 11: #Large Tile
                tile_group.add(FloorTile(col*64, row*64, True))
                tile_group.add(FloorTile(col*64+32, row*64, True))
                tile_group.add(FloorTile(col*64, row*64+32, True))
                tile_group.add(FloorTile(col*64+32, row*64+32, True))

    return tile_group
