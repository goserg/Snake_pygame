from typing import List, Tuple

import pygame

import utils.settings as s
from window_manager import window


class Cube:

    def __init__(self, position: List[int], color: Tuple[int, int, int], tag: str) -> None:
        self.color = color
        self.position = position
        self.live = True
        self.tag = tag

    def tick(self) -> None:
        n = 2
        a = self.color[0]
        b = self.color[1]
        c = self.color[2]
        a = a + n if a < 255 - n else 255
        b = b + n if b < 255 - n else 255
        c = c + n if c < 255 - n else 255
        self.color = (a, b, c)

    def draw(self) -> None:
        pygame.draw.rect(window, self.color, (self.position[0] * s.cell_size * s.scale,
                                              self.position[1] * s.cell_size * s.scale,
                                              s.cell_size * s.scale, s.cell_size * s.scale))
