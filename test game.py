import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Colorful Grid")

# Define square size and grid dimensions
square_size = 50
grid_width = 16
grid_height = 16
class Square:
    def __init__(self, x, y, size):
        self.rect = pygame.Rect(x, y, size, size)
        self.color = (255, 255, 255)  # Default color: white

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
# Create a 2D list to store the squares
grid = []
for row in range(grid_height):
    grid.append([])
    for col in range(grid_width):
        x = col * square_size
        y = row * square_size
        square = Square(x, y, square_size)
        grid[row].append(square)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                # Get the position of the mouse click
                mouse_x, mouse_y = pygame.mouse.get_pos()
                
                # Find the square that was clicked on
                clicked_row = mouse_y // square_size
                clicked_col = mouse_x // square_size
                
                # Change the color of the clicked square to a random color
                clicked_square = grid[clicked_row][clicked_col]
                clicked_square.color = (random.randint(0, 255),
                                        random.randint(0, 255),
                                        random.randint(0, 255))

    # Clear the screen
    screen.fill((0, 0, 0))
    
    # Draw the squares
    for row in grid:
        for square in row:
            square.draw()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
if __name__ == '__main__':
    main()
