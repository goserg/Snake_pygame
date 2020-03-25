import pygame
from src.Cube import Cube


class Snake(object):
    body = []

    def __init__(self, window_size, cell_size, color):
        self.window_size = window_size
        self.cell_size = cell_size
        self.color = color
        self.rows = self.window_size//self.cell_size
        self.x = 5
        self.y = 5
        self.body.append(Cube(self.x, self.y, window_size, cell_size, color))

    def move(self, direct):
        if direct is None:
            return
        self.x += direct[0]
        self.y += direct[1]
        self.body.append(Cube(self.x, self.y, self.window_size, self.cell_size, self.color))
        if len(self.body) > 15:
            self.body.pop(0)
        self.check_collision()
        for i in self.body:
            i.tick()

    def check_collision(self):
        head = self.body[-1]
        for i in self.body[:-1]:
            if i.x == head.x and i.y == head.y:
                print("collision")

    def draw(self, surface):
        for i in self.body:
            i.draw(surface)
