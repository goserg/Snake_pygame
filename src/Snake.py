from src.Cube import Cube


class Snake(object):
    def __init__(self, window_size, cell_size, color):
        self.window_size = window_size
        self.cell_size = cell_size
        self.color = color
        self.rows = self.window_size//self.cell_size
        self.position = [5, 5]
        self.dx = 0
        self.dy = 0
        self.size = 1
        self.body = []
        self.body.append(Cube(self.position, cell_size, color))

    def move(self, direct):
        self.body.append(Cube(self.position[:], self.cell_size, self.color))
        if direct is not None:
            if self.dx != -direct[0]:
                self.dx = direct[0]
            if self.dy != -direct[1]:
                self.dy = direct[1]
        self.position[0] += self.dx
        if self.position[0] >= self.window_size//self.cell_size:
            self.position[0] = 0
        elif self.position[0] < 0:
            self.position[0] = self.window_size//self.cell_size - 1
        self.position[1] += self.dy
        if self.position[1] > self.window_size//self.cell_size - 1:
            self.position[1] = 0
        elif self.position[1] < 0:
            self.position[1] = self.window_size // self.cell_size - 1
        if len(self.body) > self.size:
            self.body.pop(0)
        for i in self.body:
            i.tick()

    def check_collision(self, food, border):
        head = self.body[-1]
        for i in self.body[:-1]:
            if i.position == head.position and self.size > 3:
                print("score:", self.size - 1)
                self.__init__(self.window_size, self.cell_size, self.color)
                food.random_food()
        for b in border:
            if head.position == list(b.position):
                print("score:", self.size - 1)
                self.__init__(self.window_size, self.cell_size, self.color)
                food.random_food()
        if head.position == food.position:
            self.size += 1
            food.random_food()

    def draw(self, surface):
        for i in self.body:
            i.draw(surface)
