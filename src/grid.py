import pygame


class Grid:
    def __init__(self, window_size, cell_size, color):
        self.window_size = window_size
        self.cell_size = cell_size
        self.color = color
        self.rows = self.window_size//self.cell_size

    def draw(self, surface):
        x = 0
        y = 0
        for _ in range(self.rows):
            x += self.cell_size
            y += self.cell_size

            pygame.draw.line(surface, self.color, (x, 0), (x, self.window_size))
            pygame.draw.line(surface, self.color, (0, y), (self.window_size, y))
