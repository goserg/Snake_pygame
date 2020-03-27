import pygame


class Cube(object):

    def __init__(self, position, cell_size, color):
        self.cell_size = cell_size
        self.color = color
        self.position = position

    def tick(self):
        a = self.color[0]
        b = self.color[1]
        c = self.color[2]
        if a < 255:
            a += 2
        if b < 255:
            b += 2
        if c < 255:
            c += 2
        self.color = (a, b, c)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0] * self.cell_size, self.position[1] * self.cell_size,
                                               self.cell_size, self.cell_size))
