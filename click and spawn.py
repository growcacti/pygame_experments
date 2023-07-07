import pygame
import random

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Rectangles")
clock = pygame.time.Clock()

class Rectangle:
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.dx = random.choice([-speed, speed])
        self.dy = random.choice([-speed, speed])

    def update(self, rectangles):
        self.x += self.dx
        self.y += self.dy

        if self.x <= 0 or self.x + self.width >= width:
            self.dx *= -1
        if self.y <= 0 or self.y + self.height >= height:
            self.dy *= -1

        for other_rect in rectangles:
            if other_rect != self:
                if self.intersects(other_rect):
                    self.dx *= -1
                    self.dy *= -1
                    break

    def intersects(self, other_rect):
        return (self.x < other_rect.x + other_rect.width and
                self.x + self.width > other_rect.x and
                self.y < other_rect.y + other_rect.height and
                self.y + self.height > other_rect.y)

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))

rectangles = []
num_rectangles = 2

for _ in range(num_rectangles):
    x = random.randint(0, width - 50)
    y = random.randint(0, height - 50)
    rect_width = random.randint(10, 50)
    rect_height = random.randint(10, 50)
    speed = random.randint(1, 5)
    rectangle = Rectangle(x, y, rect_width, rect_height, speed)
    rectangles.append(rectangle)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                x, y = event.pos
                rect_width = random.randint(10, 50)
                rect_height = random.randint(10, 50)
                speed = random.randint(1, 5)
                rectangle = Rectangle(x, y, rect_width, rect_height, speed)
                rectangles.append(rectangle)

    screen.fill((255, 255, 255))

    for rectangle in rectangles:
        rectangle.update(rectangles)
        rectangle.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
