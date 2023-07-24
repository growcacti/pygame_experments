import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dice Roller")

# Define dice properties
dice_size = 100
dice_font = pygame.font.SysFont("Arial", 60)
class Die:
    def __init__(self, x, y, size):
        self.rect = pygame.Rect(x, y, size, size)
        self.value = 1
        self.color = (255, 255, 255)  # Default color: white

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

        # Draw the die's value in the center
        value_text = dice_font.render(str(self.value), True, (0, 0, 0))
        value_rect = value_text.get_rect(center=self.rect.center)
        screen.blit(value_text, value_rect)
# Create a list to store the dice
dice = []
def create_dice():
    # Clear the dice list
    dice.clear()

    # Create dice and add them to the list
    for i in range(3):
        x = (screen_width // 4) + (i * dice_size * 2)
        y = screen_height // 2 - dice_size // 2
        die = Die(x, y, dice_size)
        dice.append(die)
def roll_dice():
    for die in dice:
        die.value = random.randint(1, 6)
running = True
create_dice()  # Create the initial dice

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                # Roll the dice
                roll_dice()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the dice
    for die in dice:
        die.draw()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
