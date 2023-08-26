
import os
import pygame as pg
#from constants import Constants as con

##os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '/'))
screen = pg.display.set_mode((1200,800))
class SpriteSheet:
    def __init__(self, filename, px, py, tw, th, m, tiles, color_key = None):
        self.sheet = pg.image.load(filename)
        if color_key:
            self.sheet = self.sheet.convert()
            self.sheet.set_colorkey(color_key)
        else:
            self.sheet = self.sheet.convert_alpha()
        self.cells = [(px + tw * i, py, tw-m, th) for i in range(tiles)]
        self.index = 0

    def update(self):
        self.tile_rect = self.cells[self.index % len(self.cells)]
        self.index += 1

    def draw(self, surface, x, y):
        rect = pg.Rect(self.tile_rect)
        rect.center = (x, y) 
        surface.blit(self.sheet, rect, self.tile_rect)
        astersurf.blit(self.sheet, rect, self.tile_rect)
pg.init()
astersurf = pg.Surface((300, 300)).convert_alpha()
clock = pg.time.Clock()

sprite_sheet = SpriteSheet("ss2.png", 0, 0, 50, 50, 6, 6, (0, 128, 0))

run = True
while run:
    clock.tick(10)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    sprite_sheet.update()

    astersurf.fill(0)
    sprite_sheet.draw(astersurf, *astersurf.get_rect().center)
    pg.display.update()
    
pg.quit()
exit()

