import cube
cubes = []


def add(c: cube.Cube):
    if c not in cubes:
        cubes.append(c)


def remove(c: cube.Cube):
    cubes.remove(c)


def draw():
    for i in cubes:
        i.draw()
