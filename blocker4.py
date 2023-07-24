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
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 255, 0),  # Yellow
    (255, 0, 255),  # Magenta
    (0, 255, 255)   # Cyan
]

class Block:
    def __init__(self, x, y, size, color, velocity):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = color
        self.velocity = velocity

    def move(self, x, y):
        self.rect.x += x
        self.rect.y += y

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

def create_block(blocks):
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

    create_block(blocks)  # Create the initial block

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

        # Update the blocks
        for block in blocks:
            block.move(random.randint(1, 10), random.randint(1, 10))
            block.update()

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the blocks
        for block in blocks:
            block.draw()

        # Check for collisions between the mouse-click block and other blocks
        mouse_block = blocks[-1]  # Get the mouse-click block
        for block in blocks[:-1]:  # Exclude the mouse-click block from collision checks
            if mouse_block.rect.colliderect(block.rect):
                # Increase the size of the mouse-click block
                mouse_block.rect.inflate_ip(5, 5)
                if mouse_block.rect.width > screen_width / 5:
                    # Remove collided blocks
                    blocks.remove(block)

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

if __name__ == '__main__':
    main()
