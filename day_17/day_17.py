#! /usr/bin/env python3
"""--- Advent of Code Day 17: Conway Cubes ---"""

from typing import List, Tuple, Dict
from collections import defaultdict
from itertools import product

FILENAME = "day_17.txt"

ACTIVE = '#'
INACTIVE = '.'
CYCLES = 6


def get_directions(dimensions: int) -> List[List[int]]:
    delta = {-1, 0, 1}
    directions = list(product(delta, repeat=dimensions))
    directions.remove(tuple([0 for _ in range(dimensions)]))
    return directions


DIR_3D = get_directions(3)
DIR_4D = get_directions(4)


def get_neighbours_3d(grid: List, coord: Tuple[int, ...], directions: List[Tuple[int, ...]]) -> Dict[str, int]:
    res = defaultdict(int)
    dim_z = len(grid)
    dim_y = len(grid[0])
    dim_x = len(grid[0][0])
    for dx, dy, dz in directions:
        x, y, z = coord[0] + dx, coord[1] + dy, coord[2] + dz
        if (x in range(dim_x)) and (y in range(dim_y)) and (z in range(dim_z)):
            res[grid[z][y][x]] += 1
    return res


def get_neighbours_4d(grid: List, coord: Tuple[int, ...], directions: List[Tuple[int, ...]]) -> Dict[str, int]:
    res = defaultdict(int)
    dim_w = len(grid)
    dim_z = len(grid[0])
    dim_y = len(grid[0][0])
    dim_x = len(grid[0][0][0])
    for dx, dy, dz, dw in directions:
        x, y, z, w = coord[0] + dx, coord[1] + dy, coord[2] + dz, coord[3] + dw
        if (x in range(dim_x)) and (y in range(dim_y)) and (z in range(dim_z) and (w in range(dim_w))):
            res[grid[w][z][y][x]] += 1
    return res


def get_count(grid: List, dimensions: int):
    cnt = 0
    for i in grid:
        for j in i:
            if dimensions == 3:
                cnt += j.count(ACTIVE)
                continue
            for k in j:
                cnt += k.count(ACTIVE)
    return cnt


def add_padding_3d(grid):
    new = []
    new_dim_x = new_dim_y = len(grid[0][0]) + 2
    empty_layer = [INACTIVE * new_dim_x for _ in range(new_dim_y)]
    empty_row = INACTIVE * new_dim_x
    for layer in grid:
        tmp = []
        for row in layer:
            row = INACTIVE + row + INACTIVE
            tmp.append(row)
        tmp = [empty_row] + tmp + [empty_row]
        new.append(tmp)
    new = [empty_layer] + new + [empty_layer]
    return new


def add_padding_4d(grid):
    new = []
    new_dim_z = len(grid[0]) + 2
    new_dim_x = new_dim_y = len(grid[0][0]) + 2
    empty_layer = [INACTIVE * new_dim_x for _ in range(new_dim_y)]
    empty_cube = [empty_layer[:] for _ in range(new_dim_z)]
    empty_row = INACTIVE * new_dim_x
    for cube in grid:
        tmp_cube = []
        for layer in cube:
            tmp_layer = []
            for row in layer:
                row = INACTIVE + row + INACTIVE
                tmp_layer.append(row)
            tmp_layer = [empty_row] + tmp_layer + [empty_row]
            tmp_cube.append(tmp_layer)
        tmp_cube = [empty_layer] + tmp_cube + [empty_layer]
        new.append(tmp_cube)
    new = [empty_cube] + new + [empty_cube]
    return new


def part1(grid: List[str]) -> int:
    grid = [grid]
    for _ in range(CYCLES):
        grid = add_padding_3d(grid)
        new = []
        for z in range(len(grid)):
            layer = []
            for y in range(len(grid[0])):
                row = ""
                for x in range(len(grid[0][0])):
                    curr = grid[z][y][x]
                    neighbours = get_neighbours_3d(grid, (x, y, z), DIR_3D)
                    if (curr == ACTIVE) and (neighbours.get(ACTIVE) not in {2, 3}):
                        row += INACTIVE
                    elif (curr == INACTIVE) and (neighbours.get(ACTIVE) == 3):
                        row += ACTIVE
                    else:
                        row += curr
                layer.append(row)
            new.append(layer)
        grid = new

    return get_count(grid, 3)


def part2(grid: List[str]) -> int:
    grid = [[grid]]
    for _ in range(CYCLES):
        grid = add_padding_4d(grid)
        new = []
        for w in range(len(grid)):
            cube = []
            for z in range(len(grid[0])):
                layer = []
                for y in range(len(grid[0][0])):
                    row = ""
                    for x in range(len(grid[0][0][0])):
                        curr = grid[w][z][y][x]
                        neighbours = get_neighbours_4d(grid, (x, y, z, w), DIR_4D)
                        if (curr == ACTIVE) and (neighbours.get(ACTIVE) not in {2, 3}):
                            row += INACTIVE
                        elif (curr == INACTIVE) and (neighbours.get(ACTIVE) == 3):
                            row += ACTIVE
                        else:
                            row += curr
                    layer.append(row)
                cube.append(layer)
            new.append(cube)
        grid = new

    return get_count(grid, 4)


def main():
    with open(FILENAME) as f:
        inp = f.readlines()
        inp = [line.strip() for line in inp]
    print(f'Part 1: {part1(inp)}')
    print(f'Part 2: {part2(inp)}')


if __name__ == "__main__":
    main()
