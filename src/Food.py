import pygame
from random import randrange


class Food:
    def __init__(self, window_size, cell_size, color):
        self.window_size = window_size
        self.cell_size = cell_size
        self.color = color
        self.rows = self.window_size // self.cell_size
        self.position = [0, 0]
        self.random_food([])

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0] * self.cell_size, self.position[1] * self.cell_size,
                                               self.cell_size, self.cell_size))

    def random_food(self, occupied):
        size = self.window_size // self.cell_size
        self.position = [randrange(size), randrange(size)]
        for i in occupied:
            if i.position == self.position:
                self.random_food(occupied)
