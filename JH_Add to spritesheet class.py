import os
import random
import pygame as pg
import itertools
#os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '/rpgsprites'))

# Useful constants.
CAPTION = "sprite_sheet"
SCREEN_SIZE = (1800, 800)
BACKGROUND_COLOR = pg.Color("darkgreen")



# Set up environment.
os.environ['SDL_VIDEO_CENTERED'] = '1'
pg.init()
pg.display.set_caption(CAPTION)
pg.display.set_mode(SCREEN_SIZE)

# Load all graphics.
class SpriteSheet:
    def __init__(self, filename, px, py, tilewidth, tileheight, m, tiles):
        
        self.filename = filename        
        self.sheet = pg.image.load(self.filename).convert_alpha()
        self.size = self.sheet.get_size()
        self.total_width = self.sheet.get_width()
        self.total_height = self.sheet.get_height()
        self.total_rect = pg.Rect(self.sheet.get_rect())
       
        self.px = px
        self.py = py
        self.posx = self.px
        self.posy = self.py
        self.tilewidth = tilewidth
        self.tileheight = tileheight
        self.missing = m
        self.tiles= tiles
     
        self.rows = self.posy + self.tiles
        self.columns = self.posx + self.tiles
        
        self.x2 = self.tiles - self.missing         
        self.obj_size = self,px, self.py
        self.x = 0
        self.y = 0
        self.direct_dict = {"up": ( 0,-self.y),
                            "right" : ( self.x, 0),
                            "down"  : ( 0, self.y),
                            "left"  : (-self.x, 0)}

        self.direction = ["up","right", "down","left"]
        self.controls = {pg.K_UP    : "up",
                         pg.K_RIGHT : "right",
                         pg.K_DOWN  : "down",
                         pg.K_LEFT  : "left"}
        self.facing = self.direction
        self.newdirection = self.facing
        self.cells = [(self.px + self.tilewidth * i, self.py, self.tilewidth-self.missing, self.tileheight) for i in range(tiles)]
        self.index = 0
        self.tile_rect = self.cells[self.index % len(self.cells)]
       
    
        self.rows = self.posx + self.tilewidth
        self.columns = self.posy
        self.x2 = tilewidth- self.missing
        self.cells=[(self.rows* i, self.posy,self.x2, self.tile.height) for i in range(tiles)]
        self.index = 0
        self.get_frames(self.sheet)

    def facing(self, facing = "down"):
        self.facing = facing
    def get_frames(self, sheet):
        """Get a list of all frames."""

        self.all_frames = self.split_sheet(self.sheet, self.size, self.rows, self.columns)
        print(self.all.frames)
        return self.all_frames

    def make_frame_dict(self, frames):
   
        self.frame_dict = {}
        for i,self.direct in enumerate(self.direction):
            self.frame_dict[self.direct] = itertools.cycle([self.frames[i][0], self.frames[i][2]])
            print(self.frame)
            return frame_dict

    def adjust_images(self, now=0):
        """Update the sprites walkframes as the sprite's direction changes."""
        if self.new_direction != self.old_direction:
            self.walkframes = self.walkframe_dict[self.new_direction]
            self.old_direction = self.new_direction
            self.redraw = True
        self.make_image(now)

    def make_image(self, now):
        """Update the sprite's animation as needed."""
        if self.redraw or now-self.animate_timer > 1000/self.animate_fps:
            self.image = next(self.walkframes)
            self.animate_timer = now
        self.redraw = False

    def add_direction(self, direction):
        """Add direction to the sprite's direction stack and change current direction.
    """
        if self.newdirection in self.direction_stack:
            self.direction_stack.remove(self.newdirection)
            self.direction_stack.append(self.newdirection)
            self.newdirection = direction

    def pop_direction(self, direction):
        """
        Remove direction from direction stack and change current direction
        to the top of the stack (if not empty).
        """
        if direction in self.direction_stack:
            self.direction_stack.remove(direction)
        if self.direction_stack:
            self.direction = self.direction_stack[-1]

    def update(self, now, screen_rect):

        self.adjust_images(now)
        if self.direction_stack:
            direction_vector = self.direct_dict[self.newdirection]
            self.rect.x += self.speed*direction_vector[0]
            self.rect.y += self.speed*direction_vector[1]
            self.tile_rect = self.cells[self.index % len(self.cells)]
            self.index += 1

    def draw(self, surface):
        """Draw sprite to surface (not used if using group draw functions)."""
        surface.blit(self.image, self.rect)

    def split_sheet(self,sheet,size,columns, rows):
        """
        Divide a loaded sprite sheet into subsurfaces.

        The argument size is the width and height of each frame (w,h)
        columns and rows are the integer number of cells horizontally and
        vertically.
        """
        self.sheet = sheet
        self.size = size
        self.columns = columns
        self.row = rows
        self.subsurfaces = []
        for y in range(self.rows):
            self.row = []
        for x in range(columns): 
            self.rect = pg.Rect((x*self.size[0], y*self.size[1]), self.size)
            self.row.append(sheet.subsurface(self.rect))
            self.subsurfaces.append(self.row)
            return subsurfaces


pg.init()
window = pg.display.set_mode((400, 300))
clock = pg.time.Clock()

sprite_sheet = SpriteSheet('awesomepossum sheet.bmp', 18, 580, 64, 66, 0, 6)

run = True
while run:
    clock.tick(10)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    sprite_sheet.update()

    window.fill(0)
    sprite_sheet.draw(window, *window.get_rect().center)
    pg.display.update()
    

def load_all_gx(self, path, accept=(".png",".jpg",".bmp")):
    self.path = path
    self.accept= accept
    self.gx = {}
    for self.image in os.listdir(path):
        self.name,self.ext = os.path.splitext(self.image)
        self.images = pg.image.load(os.path.join(self.path, self.image))
        self.images = img.convert_alpha()
        self.gxlist = []
        self.gxlist = self.images[self.name]
        self.image
    return self.images





def strip_from_sheet(sheet, start, size, columns, rows=1):
    """
    Strips individual frames from a sprite sheet given a start location,
    sprite size, and number of columns and rows.
    """
    frames = []
    for j in range(rows):
        for i in range(columns):
            location = (start[0]+size[0]*i, start[1]+size[1]*j)
            frames.append(sheet.subsurface(pg.Rect(location, size)))
    return frames



pg.quit()
exit()

