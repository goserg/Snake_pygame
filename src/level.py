from typing import List

import cube

cubes: List[cube.Cube] = []


def add(c: cube.Cube) -> None:
    if c not in cubes:
        cubes.append(c)


def remove(c: cube.Cube) -> None:
    cubes.remove(c)


def draw() -> None:
    for i in cubes:
        i.draw()
