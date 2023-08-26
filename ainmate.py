# Spritesheet
# https://www.pg.org/wiki/Spritesheet)
#
# pg.Surface object
# https://www.pg.org/docs/ref/surface.html
#
# How do I create animated sprites using Sprite Sheets in pg?
# https://stackoverflow.com/questions/55200501/how-do-i-create-animated-sprites-using-sprite-sheets-in-pg/55200625#55200625
#
# Invalid destination position for blit error, not seeing how
# https://stackoverflow.com/questions/55199591/invalid-destination-position-for-blit-error-not-seeing-how/55199736#55199736
#
# GitHub - pgExamplesAndAnswers - Surface and image - Load Sprite Sheet
# https://github.com/Rabbid76/pgExamplesAndAnswers/blob/master/documentation/pg/pg_surface_and_image.md

import os
import pygame as pg


pg.init()

W = 400
H = 300


screen = pg.display.set_mode((W, H))
screen_rect = screen.get_rect()



clock = pg.time.Clock()
class SpriteSheet:
    def __init__(self, filename, px, py, tw, th, m, tiles):
        self.sheet = pg.image.load("PHT.png")
       
            
        self.sheet = self.sheet.convert_alpha()
        self.cells = [(px + tw * i, py, tw-m, th) for i in range(tiles)]
        self.index = 0

    def update(self):
        self.tile_rect = self.cells[self.index % len(self.cells)]
        self.index += 1

    def draw(self, surface, x, y):
        self.rect = pg.Rect(self.tile_rect)
        self.rect.center = (x, y) 
        surface.blit(self.sheet, self.rect, self.tile_rect)

    

#858.0 429.0 286.0 214.5 171.6 143.0 122.57142857142857
# 107.25 95.33333333333333 85.8 78.0858.0 429.0 286.0
# 214.5 171.6 143.0 122.57142857142857 107.25 95.33333333333333 85.8 78.0


sprite_sheet = SpriteSheet('PHT.png', 78, 59, 78, 59, 1, 11,)
r = SpriteSheet('PHT.png', 86,59, 78, 59, 1, 11,) 
u = SpriteSheet('PHT.png', 95,59 ,78 , 59, 1, 11,) 
d = SpriteSheet('PHT.png', 107, 59, 78, 59, 1, 11,)
u = SpriteSheet('PHT.png', 95,59 ,78 , 59, 1, 11,) 
l = SpriteSheet('PHT.png', 143, 59, 78, 59, 1, 11,) 
sprite_sheet.update()
sprite_sheet.draw(screen, *screen.get_rect().center)


v = [2, 2]
run = True
while run:
    clock.tick(10)
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pressed = pg.key.get_pressed()
    screen.set_colorkey(0)
    screen.fill(0)




    if pressed[pg.K_LEFT]:
        l.update()
        l.draw(screen, (W / 2),(H / 2))
        v =(1,0)
  
      

    if pressed [pg.K_RIGHT]:
        r.update()
        
        r.draw(screen, (W / 2),(H / 2))
        v=(-1,0)
    if pressed[pg.K_UP]:
        u.update()
        u.draw(screen, (W / 2),(H / 2))
        v=(0,1)

    if pressed [pg.K_DOWN]:
        d.update()
        d.draw(screen, (W / 2),(H / 2))
        v=(0,-1)


    pg.display.update()
    
pg.quit()
exit()

