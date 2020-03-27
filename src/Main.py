from Snake import Snake
from Grid import Grid
from Food import Food
from Border import Border
from Menu import Menu
from JoystickController import JoystickController
import pygame

scale = 1
cell_size = int(20 * scale)
window_size = int(500 * scale)
delay = 10
game_delay = 10
t = 0

pygame.init()
win = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption("Snake v0.1")

border = Border(window_size, cell_size)
snake = Snake(window_size, cell_size, color=(0, 0, 150))
grid = Grid(window_size, cell_size, color=(50, 50, 50))
food = Food(window_size, cell_size, snake, border, color=(0, 150, 0))
menu = Menu(window_size, scale)

joystick = JoystickController()


def draw():
    win.fill((0, 0, 0))

    snake.draw(win)
    food.draw(win)
    border.draw(win)

    grid.draw(win)

    if pause:
        menu.draw(win)

    pygame.display.update()


def get_direction():
    direct = joystick.get_hat()
    if direct is None:
        if keys[pygame.K_DOWN]:
            direct = (0, 1)
        elif keys[pygame.K_UP]:
            direct = (0, -1)
        elif keys[pygame.K_RIGHT]:
            direct = (1, 0)
        elif keys[pygame.K_LEFT]:
            direct = (-1, 0)
        else:
            direct = (0, 0)

    return direct


pause = True
run = True
first = True
while run:
    pygame.time.delay(delay)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if t == game_delay:
        t = 0
        if keys[pygame.K_SPACE] or joystick.is_pause_pressed():
            if pause:
                if menu.get_state() == 0:
                    pause = False
                elif menu.get_state() == 3:
                    run = False
            else:
                pause = True
            draw()
        if not pause:
            snake.move(get_direction())
            if snake.check_collision(food=food, border=border.border):
                pause = True
            draw()
        else:
            if menu.switch(joystick.get_hat(), keys):
                draw()
    if first:
        draw()
        first = False
    t += 1

pygame.quit()
