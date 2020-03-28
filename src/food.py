from cube import Cube
import utils.settings as s
from random import randrange
import level


class Food:
    def __init__(self):
        self.food = Cube([0, 0], s.food_color, "food")
        self.rows = s.window_size // s.cell_size
        self.new_position()
        level.add(self.food)

    def draw(self):
        self.food.draw()

    def new_position(self):
        size = s.window_size // s.cell_size
        self.food.position = [randrange(size), randrange(size)]
        for i in level.cubes:
            if i != self.food and i.position == self.food.position:
                self.new_position()
