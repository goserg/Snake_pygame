from Snake import Snake
from Grid import Grid
from Food import Food
from Border import Border
from Menu import Menu
from utils.JoystickController import JoystickController
import utils.Controller as Controller
import pygame

scale = 1
cell_size = int(20 * scale)
window_size = int(500 * scale)
delay = 10
game_delay = 10
t = 0

pygame.init()
win = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption("Snake v0.2")

border = Border(window_size, cell_size)
snake = Snake(window_size, cell_size, color=(0, 0, 150))
grid = Grid(window_size, cell_size, color=(50, 50, 50))
food = Food(window_size, cell_size, snake, border, color=(0, 150, 0))
menu = Menu(window_size, scale)

Controller.joystick = JoystickController()
Controller.keys = pygame.key.get_pressed()


def draw():
    win.fill((0, 0, 0))

    snake.draw(win)
    food.draw(win)
    border.draw(win)

    if menu.grid == "On":
        grid.draw(win)

    if pause:
        menu.draw(win)

    pygame.display.update()


pause = True
run = True
to_draw = True
while run:
    pygame.time.delay(delay)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    Controller.get_keys()
    if t == game_delay:
        t = 0
        if Controller.is_start_pressed():
            if pause:
                if menu.get_state() == 0:
                    pause = False
                elif menu.get_state() == 1:
                    menu.switch_grid()
                    to_draw = True
                elif menu.get_state() == 2:
                    menu.switch_scale()
                    scale = menu.scale
                    cell_size = int(20 * scale)
                    window_size = int(500 * scale)
                    win = pygame.display.set_mode((window_size, window_size))
                    border = Border(window_size, cell_size)
                    snake = Snake(window_size, cell_size, color=(0, 0, 150))
                    grid = Grid(window_size, cell_size, color=(50, 50, 50))
                    food = Food(window_size, cell_size, snake, border, color=(0, 150, 0))
                    to_draw = True
                elif menu.get_state() == 3:
                    run = False
        elif Controller.is_pause_pressed():
            pause = True
            to_draw = True
        if not pause:
            snake.move(Controller.get_direction())
            if snake.check_collision(food=food, border=border.border):
                pause = True
            to_draw = True
        else:
            if menu.switch():
                to_draw = True
    if to_draw:
        draw()
        to_draw = False
    t += 1

pygame.quit()
