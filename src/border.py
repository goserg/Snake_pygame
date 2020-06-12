from typing import List

from cube import Cube
import utils.settings as s
import level


class Border:
    def __init__(self) -> None:
        self.border: List[Cube] = []
        self.color = s.border_color
        self.generate_border()

    def generate_border(self) -> None:
        n = s.window_size//s.cell_size
        for i in range(0, n):
            if n//2 - s.gap < i < n//2 + s.gap:
                continue
            cube = Cube([0, i], self.color, "wall")
            self.border.append(cube)
            level.add(cube)
            cube = Cube([n-1, i], self.color, "wall")
            self.border.append(cube)
            level.add(cube)
            cube = Cube([i, 0], self.color, "wall")
            self.border.append(cube)
            level.add(cube)
            cube = Cube([i, n - 1], self.color, "wall")
            self.border.append(cube)
            level.add(cube)
