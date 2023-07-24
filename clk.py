import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Controlled Speed Blocks")

# Define block properties
min_block_size = 5
max_block_size = 20
block_speed = 2.0  # Adjust this value to control the overall speed

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

def create_random_block():
    x = random.randint(0, screen_width - max_block_size)
    y = random.randint(0, screen_height - max_block_size)
    size = random.randint(min_block_size, max_block_size)
    velocity = [random.choice([-1, 1]) * block_speed, random.choice([-1, 1]) * block_speed]
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return Block(x, y, size, color, velocity)

def main():
    blocks = []  # List to store the moving blocks

    # Populate the screen with random blocks
    num_blocks = 50  # Adjust the number of blocks as desired
    for _ in range(num_blocks):
        block = create_random_block()
        blocks.append(block)

    clock = pygame.time.Clock()

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

        clock.tick(60)  # Adjust the desired frame rate (e.g., 60 FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
