import pygame as pg
import random

# Initialize pg
pg.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption("Chain Reaction Blocks")

# Define block properties
min_block_size = 2
max_block_size = 20
block_speed = 1

size = (screen_width // 40, screen_height // 30)
absorber_size = size[0]
absorber_color = (255, 0, 0)

class Block(pg.sprite.Sprite):
    def __init__(self, x, y, size, color, velocity):
        super().__init__()
        self.size = size
        self.image = pg.Surface(self.size)
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = velocity

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        
        # Bounce off the screen edges
        if self.rect.left < 0 or self.rect.right > screen_width:
            self.velocity[0] *= -1
        if self.rect.top < 0 or self.rect.bottom > screen_height:
            self.velocity[1] *= -1

def create_random_block():
    x = random.randint(0, screen_width - max_block_size)
    y = random.randint(0, screen_height - max_block_size)
    size = random.randint(min_block_size, max_block_size)
    velocity = [random.choice([-1, 1]) * block_speed, random.choice([-1, 1]) * block_speed]
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return Block(x, y, (size, size), color, velocity)

def main():
    all_sprites = pg.sprite.Group()  # Group to store all sprites
    absorber = None  # Block created by a mouse click
  
    point = 0

    # Populate the screen with random blocks
    num_blocks = 50  # Adjust the number of blocks as desired
    for _ in range(num_blocks):
        block = create_random_block()
        all_sprites.add(block)
    newsize0=0
    newsize1=0
    points =0
    clock = pg.time.Clock()
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_x, mouse_y = pg.mouse.get_pos()
                    if absorber is None:
                        absorber = Block(mouse_x - absorber_size // 2, mouse_y - absorber_size // 2,
                                         size, absorber_color, [0, 0])
                        all_sprites.add(absorber)
                    else:
                        for block in all_sprites.sprites():
                            if pg.sprite.collide_rect(absorber, block):
                                newsize0 += block.size[0]
                                newsize1 += block.size[1]
                                absorber = Block(mouse_x - absorber_size // 2, mouse_y - absorber_size // 2,[newsize0,newsize1],absorber_color,[0,0])
                                bls= block.size[0] + block.size[1]
                                points += bls
                                block.kill()
                               
                                absorber = Block(mouse_x - absorber_size // 2, mouse_y - absorber_size // 2,
                                         size, absorber_color, [0, 0])
                                absorber.image = pg.Surface(absorber.size)
                                absorber.image.fill(absorber_color)
                                absorber.rect = absorber.image.get_rect(center=absorber.rect.center)
                                all_sprites.add(absorber)
                                break

        all_sprites.update()

        screen.fill((0, 0, 0))  # Clear the screen

        all_sprites.draw(screen)  # Draw all sprites onto the screen

        # Display the point value
        font = pg.font.Font(None, 36)
        point_text = font.render(f"Points: {point}", True, (255, 255, 255))
        screen.blit(point_text, (10, 10))

        pg.display.flip()
        clock.tick(60)  # Adjust the desired frame rate (e.g., 60 FPS)

    pg.quit()

if __name__ == '__main__':
    main()
