import pygame

joystick = None
keys = None


def get_keys():
    global keys
    keys = pygame.key.get_pressed()


def is_start_pressed():
    if keys[pygame.K_SPACE] or joystick.is_start_pressed():
        return True


def is_pause_pressed():
    if keys[pygame.K_ESCAPE] or joystick.is_pause_pressed():
        return True


def get_direction():
    joy_direct = joystick.get_hat()
    if keys[pygame.K_DOWN] or joy_direct == (0, 1):
        return 0, 1
    elif keys[pygame.K_UP] or joy_direct == (0, -1):
        return 0, -1
    elif keys[pygame.K_RIGHT] or joy_direct == (1, 0):
        return 1, 0
    elif keys[pygame.K_LEFT] or joy_direct == (-1, 0):
        return -1, 0
    else:
        return 0, 0
