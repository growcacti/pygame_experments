import os
import pygame as pg
from itertools import cycle

pg.init()

W = 200
H = 300

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
    "fr1": Thruster('th144.png', 0, 0, 50, 41, 0, 4),
    "fr2": Thruster('th144.png', 520, 0, 50, 41, 0, 4),
    "fr3": Thruster('th144.png', 103, 0, 50, 41, 0, 4),
    "fr4": Thruster('th144.png', 154, 0, 50, 41, 0, 4),
    "fr5": Thruster('th144.png', 206, 0, 50, 41, 0, 4),}
  
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
