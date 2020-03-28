import pygame


class Cube(object):

    def __init__(self, position, cell_size, color):
        self.cell_size = cell_size
        self.color = color
        self.position = position

    def tick(self):
        n = 2
        a = self.color[0]
        b = self.color[1]
        c = self.color[2]
        a = a + n if a < 255 - n else 255
        b = b + n if b < 255 - n else 255
        c = c + n if c < 255 - n else 255
        self.color = (a, b, c)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0] * self.cell_size, self.position[1] * self.cell_size,
                                               self.cell_size, self.cell_size))
