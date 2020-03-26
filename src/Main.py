from src.Snake import Snake
from src.Grid import Grid
from src.Food import Food
from src.Border import Border
import pygame

cell_size = 20
window_size = 500


pygame.init()
win = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption("Snake v0.1")

border = Border(window_size, cell_size)
snake = Snake(window_size, cell_size, color=(0, 0, 150))
grid = Grid(window_size, cell_size, color=(50, 50, 50))
food = Food(window_size, cell_size, snake, border, color=(0, 150, 0))


def draw():
    win.fill((0, 0, 0))

    snake.draw(win)
    food.draw(win)
    border.draw(win)

    grid.draw(win)
    pygame.display.update()


def get_direction():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        direct = (0, 1)
    elif keys[pygame.K_UP]:
        direct = (0, -1)
    elif keys[pygame.K_RIGHT]:
        direct = (1, 0)
    elif keys[pygame.K_LEFT]:
        direct = (-1, 0)
    else:
        direct = None
    return direct


run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    snake.move(get_direction())
    snake.check_collision(food=food, border=border.border)
    draw()

pygame.quit()
