import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Floating Block Absorber")

# Define block properties
min_block_size = 10
max_block_size = 30
block_speed = 1
absorber_size = screen_width // 30
absorber_color = (255, 0, 0)

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
    absorber = None  # Block created by a mouse click

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    absorber = Block(mouse_x - absorber_size // 2, mouse_y - absorber_size // 2,
                                     absorber_size, absorber_color, [0, 0])

        for block in blocks:
            block.update()

        # Check collisions between floating blocks
        for i, block in enumerate(blocks):
            for other_block in blocks[i+1:]:
                if block.rect.colliderect(other_block.rect):
                    block.velocity[0] *= -1
                    block.velocity[1] *= -1
                    other_block.velocity[0] *= -1
                    other_block.velocity[1] *= -1

        screen.fill((0, 0, 0))  # Clear the screen

        if absorber:
            absorber.draw()

        for block in blocks:
            block.draw()

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
