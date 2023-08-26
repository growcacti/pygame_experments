import os
import pygame as pg
from itertools import cycle

pg.init()

W = 60
H = 41

screen = pg.display.set_mode((W, H))
screen_rect = screen.get_rect()

clock = pg.time.Clock()

class Thruster:
    def __init__(self, filename, px, py, tw, th, rows, cols):
        self.sheet = pg.image.load(filename).convert_alpha()
        self.cells = [(px + tw * i, py, tw, th) for i in range(cols)]
        self.index = 0
        self.last_update_time = 0
        self.animation_speed = 1500  # Adjust this value to change the animation speed

    def update(self, current_time):
        if current_time - self.last_update_time > self.animation_speed:
            self.tile_rect = self.cells[self.index % len(self.cells)]
            self.index += 1
            self.last_update_time = current_time

    def draw(self, surface, x, y):
        self.rect = pg.Rect(self.tile_rect)
        self.rect.center = (x, y) 
        surface.blit(self.sheet, self.rect, self.tile_rect)




ssdict = {
    "fr2": Thruster('1443.png', 51, 0, 51, 41, 0, 12),
    "fr3": Thruster('1443.png', 103, 0, 51, 41, 0, 12),
    "fr4": Thruster('1443.png', 157, 0, 51, 41, 0, 12),
    "fr5": Thruster('1443.png', 204, 0, 51, 41, 0, 12),
    "fr6": Thruster('1443.png', 249, 0, 51, 41, 0, 12),
    "fr7": Thruster('1443.png', 300, 0, 51, 41, 0, 12),
    "fr8": Thruster('1443.png', 348, 0, 51, 41, 0, 12),
    "fr9": Thruster('1443.png', 401, 0, 51, 41, 0, 12),
    "fr10": Thruster('1443.png', 449, 0, 51, 41, 0, 12),
    "fr11": Thruster('1443.png', 503, 0, 51, 41, 0, 12),
    "fr12": Thruster('1443.png', 557, 0, 51, 41, 0, 12),
    "fr13": Thruster('1443.png', 610, 0, 51, 41, 0, 12),
    "fr14": Thruster('1443.png', 154, 0, 51, 41, 0, 12),
    "fr15": Thruster('1443.png', 199, 0, 51, 41, 0, 12),
    "fr16": Thruster('1443.png', 308, 0, 51, 41, 0, 12),}
   
  
# Create an iterator that cycles throughth the keys of the dictionary
sprite_cycle = cycle(ssdict.keys())

# Initialize the current sprite to the first key in the cycle
current_sprite = next(sprite_cycle)

run = True
while run:
    clock.tick(1)  # Cap the main game loop at 60 FPS

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pressed = pg.key.get_pressed()
    screen.set_colorkey(0)
    screen.fill(0)

    # Get the current time in milliseconds
    current_time = pg.time.get_ticks()

    # Update the current sprite's animation independently
    ssdict[current_sprite].update(current_time)

    # Draw the current sprite
    ssdict[current_sprite].draw(screen, *screen.get_rect().center)

    # Change to the next sprite by advancing the cycle
    current_sprite = next(sprite_cycle)

    pg.display.update()

pg.quit()
exit()
