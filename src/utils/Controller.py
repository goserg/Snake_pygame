import pygame


class Controller:
    joystick = None
    keys = None

    @classmethod
    def get_keys(cls):
        cls.keys = pygame.key.get_pressed()

    @classmethod
    def is_start_pressed(cls):
        if cls.keys[pygame.K_SPACE] or cls.joystick.is_start_pressed():
            return True

    @classmethod
    def is_pause_pressed(cls):
        if cls.keys[pygame.K_ESCAPE] or cls.joystick.is_pause_pressed():
            return True

    @classmethod
    def get_direction(cls):
        joy_direct = cls.joystick.get_hat()
        if cls.keys[pygame.K_DOWN] or joy_direct == (0, 1):
            return 0, 1
        elif cls.keys[pygame.K_UP] or joy_direct == (0, -1):
            return 0, -1
        elif cls.keys[pygame.K_RIGHT] or joy_direct == (1, 0):
            return 1, 0
        elif cls.keys[pygame.K_LEFT] or joy_direct == (-1, 0):
            return -1, 0
        else:
            return 0, 0
