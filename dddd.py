import pygame as pg
import random

# Initialize pg
pg.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Chain Reaction Blocks")
# Rest of the code...
block_speed = 1
min_block_size = 2
max_block_size = 20

size = (screen_width // 40, screen_height // 30)
absorber_size = size[0]
absorber_color = (255, 0, 0)

def create_random_block(absorber):
    x = random.randint(0, screen_width - max_block_size)
    y = random.randint(0, screen_height - max_block_size)
    size = random.randint(min_block_size, max_block_size)
    velocity = [random.choice([-1, 1]) * block_speed, random.choice([-1, 1]) * block_speed]
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return Block(x, y, (size, size), color, velocity)

    # Populate the screen with random blocks
  
        

def main():
    all_sprites = pg.sprite.Group()
    absorber = None
    points = 0

    # Populate the screen with random blocks
    num_blocks = 50  # Adjust the number of blocks as desired
    for _ in range(num_blocks):
        block = create_random_block(absorber)
        all_sprites.add(block)

    clock = pg.time.Clock()
    running = True
    while running:
        # ... (rest of the code remains the same)

        if absorber is None:
            # Check for the absorber inside the game loop
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        mouse_x, mouse_y = pg.mouse.get_pos()
                        absorber = Block(mouse_x - absorber_size // 2, mouse_y - absorber_size // 2,
                                         size, absorber_color, [0, 0])
                        all_sprites.add(absorber)

        all_sprites.update()
        


if __name__ == '__main__':
    main()
