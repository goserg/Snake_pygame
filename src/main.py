from snake import Snake
from grid import Grid
from food import Food
from border import Border
from menu import Menu
from utils.joystick_controller import JoystickController
import utils.controller as controller
import utils.settings as s
import pygame

delay = 10
game_delay = 10
t = 0

pygame.init()
win = pygame.display.set_mode((int(s.window_size * s.scale), int(s.window_size * s.scale)))
pygame.display.set_caption("Snake v0.2")

border = Border()
snake = Snake()
grid = Grid()
food = Food(snake, border)
menu = Menu()

controller.joystick = JoystickController()
controller.keys = pygame.key.get_pressed()


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

    controller.get_keys()
    if t == game_delay:
        t = 0
        if controller.is_start_pressed():
            if pause:
                if menu.get_state() == 0:
                    pause = False
                elif menu.get_state() == 1:
                    menu.switch_grid()
                    to_draw = True
                elif menu.get_state() == 2:
                    menu.switch_scale()
                    s.switch_scale()
                    win = pygame.display.set_mode((int(s.window_size * s.scale), int(s.window_size * s.scale)))
                    to_draw = True
                elif menu.get_state() == 3:
                    run = False
        elif controller.is_pause_pressed():
            pause = True
            to_draw = True
        if not pause:
            snake.move(controller.get_direction())
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
