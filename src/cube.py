import utils.settings as s
from window_manager import window
import pygame


class Cube:

    def __init__(self, position, color, tag):
        self.color = color
        self.position = position
        self.live = True
        self.tag = tag

    def tick(self):
        n = 2
        a = self.color[0]
        b = self.color[1]
        c = self.color[2]
        a = a + n if a < 255 - n else 255
        b = b + n if b < 255 - n else 255
        c = c + n if c < 255 - n else 255
        self.color = (a, b, c)

    def draw(self):
        pygame.draw.rect(window, self.color, (self.position[0] * s.cell_size * s.scale,
                                              self.position[1] * s.cell_size * s.scale,
                                              s.cell_size * s.scale, s.cell_size * s.scale))
