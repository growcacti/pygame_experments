import os
import pygame as pg
from itertools import cycle

pg.init()

W = 400
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




class Thrust:
    def __init__(self, player):
        self.player = player
        self.cam = self.player.camera
        
        self.ssdict = {"fr1": Thruster('th1.png', 0, 0, 32, 8, 0, 8),
                       "fr2": Thruster('th1.png', 32, 0, 32, 8, 0, 8),
                       "fr3": Thruster('th1.png', 64, 0, 32, 8, 0, 8),
                       "fr4": Thruster('th1.png', 96, 0, 32, 8, 0, 8),
                       "fr5": Thruster('th1.png', 128, 0, 32, 8, 0, 8),
                       "fr6": Thruster('th1.png', 163, 0, 32, 8, 0, 8),
                       "fr7": Thruster('th1.png', 192, 0, 32, 8, 0, 8),
                       "fr8": Thruster('th1.png', 224, 0, 32, 8, 0, 8),}
        self.sprite_cycle = cycle(ssdict.keys())
        self.current_sprite = next(self.sprite_cycle)
    def update(self):
         self.current_time = pg.time.get_ticks//2
         self.ssdict[self.current_sprite].update(self.current_time)

    def draw(self.surface):
         surface.blit(self.ssdict[self.current_sprite], -self.cam, player.rect)
        

