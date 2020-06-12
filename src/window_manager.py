import pygame

import utils.settings as s


window = pygame.display.set_mode((int(s.window_size * s.scale), int(s.window_size * s.scale)))
pygame.display.set_caption(s.window_caption)


def update_mode() -> None:
    global window
    window = pygame.display.set_mode((int(s.window_size * s.scale), int(s.window_size * s.scale)))
