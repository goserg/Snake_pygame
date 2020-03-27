import pygame
from utils.JoystickController import JoystickController


class Controller:
    def __init__(self):
        self.joystick = JoystickController()
        self.keys = pygame.key.get_pressed()

    def get_controls(self):
        self.keys = pygame.key.get_pressed()

    def is_start_pressed(self):
        self.get_controls()
        if self.keys[pygame.K_SPACE] or self.joystick.is_start_pressed():
            return True

    def is_pause_pressed(self):
        self.get_controls()
        if self.keys[pygame.K_ESCAPE] or self.joystick.is_pause_pressed():
            return True

    def get_direction(self):
        self.get_controls()
        joy_direct = self.joystick.get_hat()
        if self.keys[pygame.K_DOWN] or joy_direct == (0, 1):
            return 0, 1
        elif self.keys[pygame.K_UP] or joy_direct == (0, -1):
            return 0, -1
        elif self.keys[pygame.K_RIGHT] or joy_direct == (1, 0):
            return 1, 0
        elif self.keys[pygame.K_LEFT] or joy_direct == (-1, 0):
            return -1, 0
        else:
            return 0, 0
