from typing import List

import utils.settings as s
from cube import Cube
from food import Food
import utils.controller as controller
import level


class Snake(object):
    def __init__(self) -> None:
        self.rows = s.window_size * s.scale//s.cell_size * s.scale
        self.position = [5, 5]
        self.dx = 1
        self.dy = 0
        self.size = 1
        self.body: List[Cube] = []

        cube = Cube(self.position, s.snake_color, "snake")
        self.body.append(cube)
        level.add(cube)

    def move(self) -> None:
        direct = controller.get_direction()
        cube = Cube(self.position[:], s.snake_color, "snake")
        self.body.append(cube)
        level.add(cube)
        if direct != (0, 0):
            if self.dx != -direct[0]:
                self.dx = direct[0]
            if self.dy != -direct[1]:
                self.dy = direct[1]
        self.position[0] += self.dx
        if self.position[0] >= s.window_size//s.cell_size:
            self.position[0] = 0
        elif self.position[0] < 0:
            self.position[0] = s.window_size//s.cell_size - 1
        self.position[1] += self.dy
        if self.position[1] > s.window_size//s.cell_size - 1:
            self.position[1] = 0
        elif self.position[1] < 0:
            self.position[1] = s.window_size//s.cell_size - 1
        if len(self.body) > self.size:
            level.remove(self.body.pop(0))
        for i in self.body:
            i.tick()

    def check_collision(self, food: Food) -> bool:
        head = self.body[-1]
        for i in level.cubes:
            if i.position == head.position and i != head:
                if i.tag in ["wall", "snake"]:
                    for b in self.body:
                        level.remove(b)
                    print("score:", self.size - 1)
                    self.__init__()
                    food.new_position()
                    return True
                elif i.tag == "food":
                    self.size += 1
                    food.new_position()
