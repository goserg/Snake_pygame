from src.Cube import Cube


class Border:
    def __init__(self, window_size, cell_size):
        self.window_size = window_size
        self.cell_size = cell_size
        self.border = []
        self.color = (100, 100, 100)
        self.generate_border()

    def generate_border(self):
        n = self.window_size//self.cell_size
        for i in range(0, n):
            self.border.append(Cube([0, i], self.cell_size, self.color))
            self.border.append(Cube([n-1, i], self.cell_size, self.color))
            self.border.append(Cube([i, 0], self.cell_size, self.color))
            self.border.append(Cube([i, n-1], self.cell_size, self.color))

    def draw(self, surface):
        for i in self.border:
            i.draw(surface)
