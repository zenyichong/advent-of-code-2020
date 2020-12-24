#! /usr/bin/env python3
"""--- Advent of Code Day 24: Lobby Layout ---"""

from typing import List, Tuple, Set
from collections import defaultdict

FILENAME = "day_24.txt"

DIRECTIONS = dict(zip(['e', 'se', 'sw', 'w', 'nw', 'ne'],
                      [(1, 0), (0.5, -1), (-0.5, -1), (-1, 0), (-0.5, 1), (0.5, 1)]))


def part1(inp: List[str]) -> Tuple[int, Set[Tuple[float, float]]]:
    black = set()
    for line in inp:
        x, y = 0, 0
        i = 0
        while i < len(line):
            direction = line[i]

            if direction in {'n', 's'}:
                direction += line[i + 1]
                i += 2
            else:
                i += 1

            dx, dy = DIRECTIONS[direction]
            x += dx
            y += dy

        if (x, y) in black:
            black.remove((x, y))
        else:
            black.add((x, y))

    return len(black), black


def get_neighbour_coords(coords: Tuple[float, float]) -> List[Tuple[float, float]]:
    res = []
    for dx, dy in DIRECTIONS.values():
        x, y = coords[0] + dx, coords[1] + dy
        res.append((x, y))
    return res


def part2(black_tiles: Set[Tuple[int, int]]) -> int:
    for _ in range(100):
        new_black_tiles = set()
        for curr in black_tiles:
            to_check = get_neighbour_coords(curr)
            for coords in to_check + [curr]:
                num_black = 0
                for nb in get_neighbour_coords(coords):
                    if nb in black_tiles:
                        num_black += 1

                if coords in black_tiles and num_black in {1, 2}:
                    new_black_tiles.add(coords)
                elif coords not in black_tiles and num_black == 2:
                    new_black_tiles.add(coords)

        black_tiles = new_black_tiles

    return len(black_tiles)


def main():
    with open(FILENAME) as f:
        inp = f.readlines()
        inp = [line.strip() for line in inp]
    ans_p1, black_tiles = part1(inp)
    print(f'Part 1: {ans_p1}')
    print(f'Part 2: {part2(black_tiles)}')


if __name__ == "__main__":
    main()
