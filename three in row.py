import pygame
import random

pygame.init()

# Set up the screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Color Matching Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define block size and grid dimensions
BLOCK_SIZE = 40
GRID_WIDTH, GRID_HEIGHT = SCREEN_WIDTH // BLOCK_SIZE, SCREEN_HEIGHT // BLOCK_SIZE
def get_random_color():
    
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


    return random.choice([(r, g, 255), (r, 255, b), (255, g, b)])  # You can add more colors if you like
def create_random_grid():
    grid = []
    for y in range(GRID_HEIGHT):
        row = [get_random_color() for _ in range(GRID_WIDTH)]
        grid.append(row)
    return grid
def check_matching(grid, x, y):
    color = grid[y][x]
    if x > 1 and grid[y][x - 1] == color and grid[y][x - 2] == color:
        return True
    if x < GRID_WIDTH - 2 and grid[y][x + 1] == color and grid[y][x + 2] == color:
        return True
    if y > 1 and grid[y - 1][x] == color and grid[y - 2][x] == color:
        return True
    if y < GRID_HEIGHT - 2 and grid[y + 1][x] == color and grid[y + 2][x] == color:
        return True
    return False
def check_matching(grid, x, y):
    color = grid[y][x]
    if x > 1 and grid[y][x - 1] == color and grid[y][x - 2] == color:
        return True
    if x < GRID_WIDTH - 2 and grid[y][x + 1] == color and grid[y][x + 2] == color:
        return True
    if y > 1 and grid[y - 1][x] == color and grid[y - 2][x] == color:
        return True
    if y < GRID_HEIGHT - 2 and grid[y + 1][x] == color and grid[y + 2][x] == color:
        return True
    return False
def main():
    grid = create_random_grid()
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Add game logic here:
        # - Check for user clicks on matching blocks
        # - Update the grid and score accordingly
        # - Call replace_matching_blocks() when necessary

        screen.fill(BLACK)
        # Draw the grid
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                pygame.draw.rect(screen, grid[y][x], (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

        pygame.display.flip()
        clock.tick(30)  # Set the frame rate (adjust as needed)

    pygame.quit()

if __name__ == "__main__":
    main()
