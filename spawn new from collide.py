import pygame as pg
import random

pg.init()
width, height = 800, 600
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Moving Rectangles")
clock = pg.time.Clock()

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

                    # Create a new rectangle at a random position
                    new_x = random.randint(0, width - 50)
                    new_y = random.randint(0, height - 50)
                    new_width = random.randint(10, 50)
                    new_height = random.randint(10, 50)
                    new_speed = random.randint(1, 5)
                    new_rectangle = Rectangle(new_x, new_y, new_width, new_height, new_speed)
                    rectangles.append(new_rectangle)
                    break

    def intersects(self, other_rect):
        return (self.x < other_rect.x + other_rect.width and
                self.x + self.width > other_rect.x and
                self.y < other_rect.y + other_rect.height and
                self.y + self.height > other_rect.y)

    def draw(self):
        pg.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))

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
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill((255, 255, 255))

    for rectangle in rectangles:
        rectangle.update(rectangles)
        rectangle.draw()

    pg.display.flip()
    clock.tick(60)

pg.quit()
