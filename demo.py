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
color_change_rate = 1  # Rate of color change (lower values mean slower color change)
block_color_range = (50, 205)  # Range for RGB values of block colors

class Block:
    def __init__(self, x, y, size, color, velocity):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = color
        self.velocity = velocity

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        # Wrap around if block goes off the screen
        if self.rect.right < 0:
            self.rect.left = screen_width
        elif self.rect.left > screen_width:
            self.rect.right = 0
        if self.rect.bottom < 0:
            self.rect.top = screen_height
        elif self.rect.top > screen_height:
            self.rect.bottom = 0

        # Slowly change the color of the block
        self.color = self.change_color(self.color, color_change_rate)

    @staticmethod
    def change_color(color, change_rate):
        # Change the color components based on the change rate
        r, g, b = color
        r += random.randint(-change_rate, change_rate)
        g += random.randint(-change_rate, change_rate)
        b += random.randint(-change_rate, change_rate)

        # Ensure the color components stay within the valid range
        r = max(min(r, block_color_range[1]), block_color_range[0])
        g = max(min(g, block_color_range[1]), block_color_range[0])
        b = max(min(b, block_color_range[1]), block_color_range[0])

        return (r, g, b)

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

def create_blocks(num_blocks):
    blocks = []
    for _ in range(num_blocks):
        x = random.randint(0, screen_width - block_max_size)
        y = random.randint(0, screen_height - block_max_size)
        size = random.randint(block_min_size, block_max_size)
        velocity = [random.choice([-1, 1]) * block_speed, random.choice([-1, 1]) * block_speed]
        color = (random.randint(*block_color_range), random.randint(*block_color_range), random.randint(*block_color_range))
        block = Block(x, y, size, color, velocity)
        blocks.append(block)
    return blocks

def main():
    # Create a list to store the floating blocks
    blocks = create_blocks(20)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update the blocks
        for block in blocks:
            block.update()

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the blocks
        for block in blocks:
            block.draw()

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()

if __name__ == '__main__':
    main()
