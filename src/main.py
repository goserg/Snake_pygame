from snake import Snake
from grid import Grid
from food import Food
from border import Border
from menu import Menu
import window_manager
from window_manager import window
from utils.joystick_controller import JoystickController
import utils.controller as controller
import utils.settings as s
import pygame
import level

pygame.init()

border = Border()
snake = Snake()
grid = Grid()
food = Food()
menu = Menu()

controller.joystick = JoystickController()
controller.keys = pygame.key.get_pressed()


def draw():
    window.fill((0, 0, 0))

    level.draw()

    if s.grid:
        grid.draw()

    if pause:
        menu.draw()

    pygame.display.update()


pause = True
run = True
to_draw = True
t = 0
while run:
    pygame.time.delay(s.main_loop_delay)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    controller.get_keys()
    if t == s.game_update_delay:
        t = 0
        if controller.is_start_pressed():
            if pause:
                if menu.get_state() == 0:
                    pause = False
                elif menu.get_state() == 1:
                    s.grid = not s.grid
                    to_draw = True
                elif menu.get_state() == 2:
                    s.switch_scale()
                    window_manager.update_mode()
                    to_draw = True
                elif menu.get_state() == 3:
                    run = False
        elif controller.is_pause_pressed():
            pause = True
            to_draw = True
        if not pause:
            snake.move()
            if snake.check_collision(food):
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
