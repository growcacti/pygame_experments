import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Floating Blocks")

# Define block properties
block_min_size = 10
block_max_size = 50
block_speed = 2
block_color = (255, 255, 255)

# Define colors for new blocks
new_block_colors = [
    (255, 0, 0),  # Red
    (0, 255, 0),  # Green
    (0, 0, 255),  # Blue
    (255, 255, 0),  # Yellow
    (255, 0, 255),  # Magenta
    (0, 255, 255)  # Cyan
]

class Block:
    def __init__(self, x, y, size, color, velocity):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = color
        self.velocity = velocity

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)


def create_block():
    x = random.randint(0, screen_width - block_max_size)
    y = random.randint(0, screen_height - block_max_size)
    size = random.randint(block_min_size, block_max_size)
    velocity = [random.choice([-1, 1]) * block_speed, random.choice([-1, 1]) * block_speed]
    color = random.choice(new_block_colors)
    block = Block(x, y, size, color, velocity)
    blocks.append(block)


def main():
    # Create a list to store the floating blocks
    blocks = []

    create_block()  # Create the initial block

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    # Create a new block at the mouse position
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    new_block = Block(mouse_x, mouse_y, block_min_size, block_color, [0, 0])
                    blocks.append(new_block)

        # Clear the screen
        screen.fill((0, 0, 0))

        # Update and draw the blocks
        for block in blocks:
            block.update()
            block.draw()

        # Check for collisions and update block sizes
        for block in blocks:
            for other_block in blocks:
                if block != other_block and block.rect.colliderect(other_block.rect):
                    block.rect.inflate_ip(1, 1)
                    other_block.rect.inflate_ip(1, 1)
                else:
                    block.rect.inflate_ip(-1, -1)

        # Remove blocks that have shrunk to the minimum size
        blocks = [block for block in blocks if block.rect.width > block_min_size]

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()


if __name__ == '__main__':
    main()
