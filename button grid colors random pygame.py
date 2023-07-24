import pygame as pg
import random
import sys

pg.init()

# Constants
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 6, 6
BUTTON_SIZE = 100
MARGIN = 10
GRID_WIDTH = COLS * (BUTTON_SIZE + MARGIN) + MARGIN
GRID_HEIGHT = ROWS * (BUTTON_SIZE + MARGIN) + MARGIN
clock = pg.time.Clock()
# Function to generate random colors
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Function to draw buttons
def draw_buttons(screen):
    for row in range(ROWS):
        for col in range(COLS):
            color = random_color()
            button_rect = pg.Rect(
                MARGIN + col * (BUTTON_SIZE + MARGIN),
                MARGIN + row * (BUTTON_SIZE + MARGIN),
                BUTTON_SIZE,
                BUTTON_SIZE,
            )
            pg.draw.rect(screen, color, button_rect)

# Main function
def main():
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("pg Button Grid")
    clock = pg.time.Clock()

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    x, y = event.pos
                    col = (x - MARGIN) // (BUTTON_SIZE + MARGIN)
                    row = (y - MARGIN) // (BUTTON_SIZE + MARGIN)
                    if 0 <= col < COLS and 0 <= row < ROWS:
                        # Display the button position as a text message
                        print(f"Button clicked: Row {row + 1}, Column {col + 1}")

        screen.fill((255, 255, 255))
        draw_buttons(screen)
        pg.display.flip()
        clock.tick(1)

if __name__ == "__main__":
    main()
