


import sys
import os
import pygame as pg
from pygame.math import Vector2



#os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '/rpgsprites'))

pg.init()

W = 1600
H = 800
W2 = W*2
H2 = H*2
HW = W/2
HH= H/2
screen = pg.display.set_mode((W, H))
screen_rect = screen.get_rect()






clock = pg.time.Clock()
class Player:
    def __init__(self, filename, px, py, tw, th, m, tiles):
        self.sheet = pg.image.load("ex.png")
        self.camsurf = pg.Surface((HW,HH))
        self.camx = 0
        self.camy = 0
        self.camrect = pg.Rect(self.camx,self.camy,W,H)
        self.cam = self.camx, self.camy
  
        self.sheet = self.sheet.convert_alpha()
           
        self.rect = pg.Rect(px,py,tw,th)
        self.position= Vector2(px, py)
        self.collider = self.rect.copy()
        self.old_rect = self.rect
        self.cells = [(px + tw * i, py, tw-m, th) for i in range(tiles)]
        self.index = 0
        self.font = pg.font.Font(None, 20)
    def update(self):
        self.text1 = self.font.render("position: " + str(self.position), True, [255,255,255])
        self.text2 = self.font.render("cam: " + str(self.cam), True, [255,255,255])

        self.tile_rect = self.cells[self.index % len(self.cells)]
        self.index += 1
        return self.tile_rect

    def draw(self, surface, x, y):
        self.tile_rect = self.cells[self.index % len(self.cells)]
        
        self.rect = pg.Rect(self.tile_rect)
        
        self.rect.center = (x, y)
        self.position = self.rect.center
        surface.blit(self.sheet, self.rect, self.tile_rect)
        surface.blit(self.camsurf, self.camrect, self.tile_rect)
        self.text1 = self.font.render("position: " + str(self.position), True, [255,255,255])
        self.text2 = self.font.render("cam: " + str(self.cam), True, [255,255,255])
        screen.blit(self.text1, (W - 200, H - 750))
        screen.blit(self.text2, (W - 200, H - 650))




def main():
    player = Player('gx/charactors/ex.png', 0, 0, 195, 140, 0, 10)
    still = Player('gx/charactors/ex.png', 0, 195, 140, 36, 0, 10)
    
    r = Player('gx/charactors/ex.png', 2,0 , 195, 140, 0, 10,)
    l = Player('gx/charactors/ex.png', 0, 195, 32, 140, 0, 10)
    u = Player('gx/charactors/ex.png', 0, 0, 195, 140, 0, 10)
    d = Player('gx/charactors/ex.png', 0, 72, 195, 140, 0, 10)
   
    player.draw(screen, *screen.get_rect().center)
   
    
    facing = "down"
    pp = [0, 0]
    v = [0, 0]
    run = True
    while run:
        clock.tick(10)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.quit()
                sys.exit()

        pressed = pg.key.get_pressed()
        screen.set_colorkey(0)
        screen.fill((0,180,0))
        
##        side_call = wall.get_collision_side(wall.rect,player.collider)
##        if side_call == "left":
##           player.rect.left = wall.rect.right
           
  
        player.update()
        if facing == "down":
            d.draw(screen, (W/2),(H/2)) 

        elif facing == "left":
            l.draw(screen, (W/2),(H/2)) 
        elif facing == "right":
            r.draw(screen, (W/2),(H/2)) 
        
        elif facing == "up":
            u.draw(screen, (W/2),(H/2)) 


        
        if pressed[pg.K_LEFT]:
            facing = "left"
            l.update()
            l.draw(screen, (W / 2),(H / 2))
                           
       
            v =[15,0]
            pp = [-15,0]
            screen_rect.move_ip(v)
            
            player.camrect.move_ip(pp)
           
        
          
        

        if pressed [pg.K_RIGHT]:

            facing = "right"
            r.update()
           
            r.draw(screen, (W / 2),(H / 2))
            
      
            v =[-15,0]
            pp = [15,0]
            screen_rect.move_ip(v)
            player.camrect.move_ip(pp)
           
        
          
        if pressed[pg.K_UP]:
           
            facing = "up"
            u.update()
            u.draw(screen, (W / 2),(H / 2))
            
            v =[0,15]
            pp = [0,-15]
            screen_rect.move_ip(v)
             
            player.camrect.move_ip(pp)
               
            
               
        if pressed [pg.K_DOWN]:
            d.update()
            face = "down"
            d.draw(screen, (W / 2),(H / 2))
            
      
            v =[0,-15]
            pp = [0, 15]
            screen_rect.move_ip(v)
            
            player.camrect.move_ip(pp)
           
        
               
        player.camx = player.camrect.centerx
        player.camy = player.camrect.centery
       
        pg.display.update()
       

if __name__ == '__main__':
    main()
    



