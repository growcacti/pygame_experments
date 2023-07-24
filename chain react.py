import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Chain Reaction Blocks")

# Define block properties
min_block_size = 5
max_block_size = 30
block_speed = 1
chain_reaction_threshold = 5  # Number of collisions required for a chain reaction
chain_reaction_growth = screen_width // 5  # Size increase during a chain reaction

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
    blocks = []  # List to store the floating blocks
    chain_reaction_blocks = []  # List to store blocks involved in chain reactions

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    new_block = create_random_block()
                    new_block.rect.center = (mouse_x, mouse_y)
                    blocks.append(new_block)
                    chain_reaction_blocks = [new_block]  # Start a new chain reaction

        for block in blocks:
            block.update()

        # Check collisions between chain reaction blocks and other blocks
        for chain_block in chain_reaction_blocks:
            for block in blocks:
                if chain_block != block and chain_block.rect.colliderect(block.rect):
                    block_size = block.rect.width + chain_reaction_growth
                    block.rect.size = (block_size, block_size)
                    if block not in chain_reaction_blocks:
                        chain_reaction_blocks.append(block)

        # Remove small blocks and stop the chain reaction
        for block in chain_reaction_blocks:
            if block.rect.width <= min_block_size:
                blocks.remove(block)
        chain_reaction_blocks.clear()

        screen.fill((0, 0, 0))  # Clear the screen

        for block in blocks:
            block.draw()

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
