import utils.settings as s
import pygame
from random import randrange


class Food:
    def __init__(self, snake, border):
        self.rows = s.window_size // s.cell_size
        self.position = [0, 0]
        self.snake = snake
        self.border = border
        self.random_food()

    def draw(self, surface):
        pygame.draw.rect(surface, s.food_color, (self.position[0] * s.cell_size * s.scale,
                                                 self.position[1] * s.cell_size * s.scale,
                                                 s.cell_size * s.scale,
                                                 s.cell_size * s.scale))

    def random_food(self):
        size = s.window_size // s.cell_size
        self.position = [randrange(size), randrange(size)]
        for i in self.snake.body:
            if i.position == self.position:
                self.random_food()
        for i in self.border.border:
            if i.position == self.position:
                self.random_food()
