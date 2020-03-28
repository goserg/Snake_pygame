import utils.settings as s
from cube import Cube


class Snake(object):
    def __init__(self):
        self.rows = s.window_size * s.scale//s.cell_size * s.scale
        self.position = [5, 5]
        self.dx = 1
        self.dy = 0
        self.size = 1
        self.body = []
        self.body.append(Cube(self.position, s.snake_color))

    def move(self, direct):
        self.body.append(Cube(self.position[:], s.snake_color))
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
            self.body.pop(0)
        for i in self.body:
            i.tick()

    def check_collision(self, food, border):
        head = self.body[-1]
        for i in self.body[:-1]:
            if i.position == head.position and self.size > 3:
                print("score:", self.size - 1)
                self.__init__()
                food.random_food()
                return True
        for b in border:
            if head.position == list(b.position):
                print("score:", self.size - 1)
                self.__init__()
                food.random_food()
                return True
        if head.position == food.position:
            self.size += 1
            food.random_food()

    def draw(self, surface):
        for i in self.body:
            i.draw(surface)
