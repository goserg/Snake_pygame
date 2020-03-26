import pygame
from random import randrange


class Food:
    def __init__(self, window_size, cell_size, snake, border, color):
        self.window_size = window_size
        self.cell_size = cell_size
        self.color = color
        self.rows = self.window_size // self.cell_size
        self.position = [0, 0]
        self.snake = snake
        self.border = border
        self.random_food()

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0] * self.cell_size, self.position[1] * self.cell_size,
                                               self.cell_size, self.cell_size))

    def random_food(self):
        size = self.window_size // self.cell_size
        self.position = [randrange(size), randrange(size)]
        for i in self.snake.body:
            if i.position == self.position:
                self.random_food()
        for i in self.border.border:
            if i.position == self.position:
                self.random_food()
