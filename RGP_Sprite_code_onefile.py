import random
import itertools
import pygame as pg

import prepare
import tools


SPRITE_SIZE = (32, 36)


class RPGSprite(pg.sprite.Sprite):
    """Base class for player and AI sprites."""

    def __init__(self, pos, speed, name, facing="DOWN", *groups):
        super(RPGSprite, self).__init__(*groups)
        self.speed = speed
        self.name = name
        self.direction = facing
        self.old_direction = None
        self.direction_stack = []
        self.redraw = True
        self.animate_timer = 0.0
        self.animate_fps = 10.0
        self.walkframes = None
        self.walkframe_dict = self.make_frame_dict(self.get_frames(name))
        self.adjust_images()
        self.rect = self.image.get_rect(center=pos)

    def get_frames(self, character):
        """Get a list of all frames."""
        sheet = prepare.GFX[character]
        all_frames = tools.split_sheet(sheet, SPRITE_SIZE, 3, 4)
        return all_frames

    def make_frame_dict(self, frames):
        """Create a dictionary of animation cycles for each direction."""
        frame_dict = {}
        for i, direct in enumerate(prepare.DIRECTIONS):
            frame_dict[direct] = itertools.cycle([frames[i][0], frames[i][2]])
        return frame_dict

    def adjust_images(self, now=0):
        """Update the sprites walkframes as the sprite's direction changes."""
        if self.direction != self.old_direction:
            self.walkframes = self.walkframe_dict[self.direction]
            self.old_direction = self.direction
            self.redraw = True
        self.make_image(now)

    def make_image(self, now):
        """Update the sprite's animation as needed."""
        if self.redraw or now - self.animate_timer > 1000 / self.animate_fps:
            self.image = next(self.walkframes)
            self.animate_timer = now
        self.redraw = False

    def add_direction(self, direction):
        """
        Add direction to the sprite's direction stack and change current
        direction.
        """
        if direction in self.direction_stack:
            self.direction_stack.remove(direction)
        self.direction_stack.append(direction)
        self.direction = direction

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
        """Update image and position of sprite."""
        self.adjust_images(now)
        if self.direction_stack:
            direction_vector = prepare.DIRECT_DICT[self.direction]
            self.rect.x += self.speed * direction_vector[0]
            self.rect.y += self.speed * direction_vector[1]

    def draw(self, surface):
        """Draw sprite to surface (not used if using group draw functions)."""
        surface.blit(self.image, self.rect)


class Player(RPGSprite):
    """This class will represent the user controlled character."""

    def __init__(self, pos, speed, name="warrior_m", facing="DOWN", *groups):
        super(Player, self).__init__(pos, speed, name, facing, *groups)

    def get_event(self, event):
        """Handle events pertaining to player control."""
        if event.type == pg.KEYDOWN:
            self.add_direction(event.key)
        elif event.type == pg.KEYUP:
            self.pop_direction(event.key)

    def update(self, now, screen_rect):
        """Call base classes update method and clamp player to screen."""
        super(Player, self).update(now, screen_rect)
        self.rect.clamp_ip(screen_rect)

    def add_direction(self, key):
        """Remove direction from stack if corresponding key is released."""
        if key in prepare.CONTROLS:
            super(Player, self).add_direction(prepare.CONTROLS[key])

    def pop_direction(self, key):
        """Add direction to stack if corresponding key is pressed."""
        if key in prepare.CONTROLS:
            super(Player, self).pop_direction(prepare.CONTROLS[key])


class AISprite(RPGSprite):
    """A non-player controlled sprite."""

    def __init__(self, pos, speed, name, facing, *groups):
        super(AISprite, self).__init__(pos, speed, name, facing, *groups)
        self.wait_range = (500, 2000)
        self.wait_delay = random.randint(*self.wait_range)
        self.wait_time = 0.0
        self.change_direction()

    def update(self, now, screen_rect):
        """
        Choose a new direction if wait_time has expired or the sprite
        attempts to leave the screen.
        """
        if now - self.wait_time > self.wait_delay:
            self.change_direction(now)
        super(AISprite, self).update(now, screen_rect)
        if not screen_rect.contains(self.rect):
            self.change_direction(now)
            self.rect.clamp_ip(screen_rect)

    def change_direction(self, now=0):
        """
        Empty the stack and choose a new direction.  The sprite may also
        choose not to go idle (choosing direction=None)
        """
        self.direction_stack = []
        direction = random.choice(prepare.DIRECTIONS + (None,))
        if direction:
            super(AISprite, self).add_direction(direction)
        self.wait_delay = random.randint(*self.wait_range)
        self.wait_time = now


import os
import pygame as pg


def load_all_gfx(directory, colorkey=None, accept=(".png", ".jpg", ".bmp")):
    """
    Load all graphics with extensions in the accept argument.  If alpha
    transparency is found in the image the image will be converted using
    convert_alpha().  If no alpha transparency is detected image will be
    converted using convert() and colorkey will be set to colorkey.
    """
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                if colorkey:
                    img.set_colorkey(colorkey)
            graphics[name] = img
    return graphics


def split_sheet(sheet, size, columns, rows):
    """
    Divide a loaded sprite sheet into subsurfaces.

    The argument size is the width and height of each frame (w,h)
    columns and rows are the integer number of cells horizontally and
    vertically.
    """
    subsurfaces = []
    for y in range(rows):
        row = []
        for x in range(columns):
            rect = pg.Rect((x * size[0], y * size[1]), size)
            row.append(sheet.subsurface(rect))
        subsurfaces.append(row)
    return subsurfaces


import os
import pygame as pg
import tools


# Useful constants.
CAPTION = "Drawing Order"
SCREEN_SIZE = (500, 500)
BACKGROUND_COLOR = pg.Color("darkgreen")


DIRECT_DICT = {"UP": (0, -1), "RIGHT": (1, 0), "DOWN": (0, 1), "LEFT": (-1, 0)}


DIRECTIONS = ("UP", "RIGHT", "DOWN", "LEFT")


CONTROLS = {pg.K_UP: "UP", pg.K_RIGHT: "RIGHT", pg.K_DOWN: "DOWN", pg.K_LEFT: "LEFT"}


# Set up environment.
os.environ["SDL_VIDEO_CENTERED"] = "1"
pg.init()
pg.display.set_caption(CAPTION)
pg.display.set_mode(SCREEN_SIZE)

# Load all graphics.
GFX = tools.load_all_gfx("rpgsprites")
import sys
import random
import pygame as pg

# Importing prepare initializes the display.
import prepare
import actors


class App(object):
    """This is the main class that runs the program."""

    def __init__(self):
        self.screen = pg.display.get_surface()
        self.screen_rect = self.screen.get_rect()
        self.clock = pg.time.Clock()
        self.fps = 60
        self.done = False
        self.all_sprites = pg.sprite.Group()
        self.player = actors.Player(self.screen_rect.center, 3)
        self.all_sprites.add(self.player)
        self.make_npcs()

    def make_npcs(self):
        """Create a group of NPCs and add them to the all_sprites group."""
        for name in prepare.GFX:
            if name != self.player.name:
                pos = [random.randint(50, 400), random.randint(50, 400)]
                speed = random.randint(1, 2)
                way = random.choice(prepare.DIRECTIONS)
                actors.AISprite(pos, speed, name, way, self.all_sprites)

    def event_loop(self):
        """
        Process all events.
        Send event to player so that they can also handle the event.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            self.player.get_event(event)

    def display_fps(self):
        """Show the program's FPS in the window handle."""
        template = "{} - FPS: {:.2f}"
        caption = template.format(prepare.CAPTION, self.clock.get_fps())
        pg.display.set_caption(caption)

    def update(self):
        """Update all actors."""
        now = pg.time.get_ticks()
        self.all_sprites.update(now, self.screen_rect)

    def render(self):
        """Fill screen and render all actors."""
        self.screen.fill(prepare.BACKGROUND_COLOR)
        self.all_sprites.draw(self.screen)
        pg.display.update()

    def main_loop(self):
        """
        The main game loop for the whole program.
        Process events; update; render.
        """
        while not self.done:
            self.event_loop()
            self.update()
            self.render()
            self.clock.tick(self.fps)
            self.display_fps()


def main():
    """Create an App and start the program."""
    App().main_loop()
    pg.quit()
    sys.exit()


if __name__ == "__main__":
    main()
