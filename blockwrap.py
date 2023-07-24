import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Wrapping Blocks")

# Define block properties
min_block_size = 5
max_block_size = 20
block_speed = 5
class Block:
    def __init__(self, x, y, size, color, velocity):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = color
        self.velocity = velocity

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        # Wrap around the screen
        if self.rect.left > screen_width:
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = screen_width
        if self.rect.top > screen_height:
            self.rect.bottom = 0
        elif self.rect.bottom < 0:
            self.rect.top = screen_height

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

def create_random_block():
    x = random.randint(0, screen_width - max_block_size)
    y = random.randint(0, screen_height - max_block_size)
    size = random.randint(min_block_size, max_block_size)
    velocity = [random.choice([-1, 1]), random.choice([1, -1])]
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return Block(x, y, size, color, velocity)

def main():
    blocks = []  # List to store the moving blocks

    # Populate the screen with random blocks
    num_blocks = 50  # Adjust the number of blocks as desired
    for _ in range(num_blocks):
        block = create_random_block()
        blocks.append(block)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for block in blocks:
            block.update()

        screen.fill((0, 0, 0))  # Clear the screen

        for block in blocks:
            block.draw()

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
