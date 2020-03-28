from window_manager import window
import utils.settings as s
import pygame


class Grid:
    def __init__(self):
        self.rows = s.window_size//s.cell_size

    def draw(self):
        x = 0
        y = 0
        for _ in range(self.rows):
            x += s.cell_size * s.scale
            y += s.cell_size * s.scale

            pygame.draw.line(window, s.grid_color, (x, 0), (x, s.window_size * s.scale))
            pygame.draw.line(window, s.grid_color, (0, y), (s.window_size * s.scale, y))
