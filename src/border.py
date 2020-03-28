from cube import Cube
import utils.settings as s


class Border:
    def __init__(self):
        self.border = []
        self.color = s.border_color
        self.generate_border()

    def generate_border(self):
        n = s.window_size//s.cell_size
        for i in range(0, n):
            if n//2 - s.gap < i < n//2 + s.gap:
                continue
            self.border.append(Cube([0, i], self.color))
            self.border.append(Cube([n-1, i], self.color))
            self.border.append(Cube([i, 0], self.color))
            self.border.append(Cube([i, n-1], self.color))

    def draw(self):
        for i in self.border:
            i.draw()
