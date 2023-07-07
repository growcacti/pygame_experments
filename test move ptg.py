import pygame as pg
import random



pg.init()
width, height = 1200, 600
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

    def update(self):
        self.x += self.dx
        self.y += self.dy

        # Check if the rectangle reaches the screen edges, reverse the direction if true
        if self.x <= 0 or self.x + self.width >= width:
            self.dx *= -1
        if self.y <= 0 or self.y + self.height >= height:
            self.dy *= -1

    def draw(self):
        pg.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))
# Step 4: Create the rectangles
rectangles = []
num_rectangles = 10  # Number of rectangles you want to create

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
        rectangle.update()
        rectangle.draw()

    pg.display.flip()
    clock.tick(60)  # Limit the frame rate to 60 FPS

pg.quit()

