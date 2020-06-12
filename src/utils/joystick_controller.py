from typing import Tuple

import pygame


class JoystickController:
    def __init__(self) -> None:
        if pygame.joystick.get_count() > 0:
            self.enabled = True
            self.joystick = pygame.joystick.Joystick(0)
            print("{} enabled".format(self.joystick.get_name()))
            self.joystick.init()
            self.pause = 0
        else:
            self.enabled = False

    def get_hat(self) -> Tuple[int, int]:
        if self.enabled:
            hat = self.joystick.get_hat(0)
            hat_right = hat[0]
            hut_up = hat[1]
            if hat_right != 0:
                return hat_right, 0
            return 0, -hut_up

    def is_pause_pressed(self) -> int:
        if self.enabled:
            return self.joystick.get_button(7)

    def is_start_pressed(self) -> int:
        if self.enabled:
            return self.joystick.get_button(0)
