






mport os
import pygame as pg


pg.init()

W = 400
H = 300
screen = pg.display.set_mode((W, H))
screen_rect = screen.get_rect()
background = pg.image.load("rpgsprites/scape.png")
bg_rect = background.get_rect()
screen = pg.display.set_mode((W, H))
screen_rect = screen.get_rect()
background = pg.image.load("rpgsprites/scape.png")
bg_rect = background.get_rect()

clock = pg.time.Clock()
