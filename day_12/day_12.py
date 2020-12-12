#! /usr/bin/env python3
"""--- Advent of Code Day 12: Rain Risk ---"""

from typing import List, Tuple
import numpy as np

FILENAME = "day_12.txt"

DIRECTIONS = dict(zip("NSEW", [[0, 1], [0, -1], [1, 0], [-1, 0]]))

WAYPOINT = (10, 1)
RIGHT = np.array([[0, 1], [-1, 0]])
LEFT = np.array([[0, -1], [1, 0]])


def rotate(action: str, deg: int, curr: List[int]) -> List[int]:
    if action == "R":
        for _ in range(deg // 90):
            curr = RIGHT @ np.array(curr)
    elif action == "L":
        for _ in range(deg // 90):
            curr = LEFT @ np.array(curr)
    return curr


def part1(inp: List[str]) -> int:
    heading = DIRECTIONS["E"]
    x, y = 0, 0
    for line in inp:
        action = line[0]
        amount = int(line[1:])
        if action == "F":
            dx, dy = heading
        elif action in {"R", "L"}:
            heading = rotate(action, amount, heading)
            dx, dy = heading
            continue
        else:
            dx, dy = DIRECTIONS[action]
        x += amount * dx
        y += amount * dy
    return abs(x) + abs(y)


def part2(inp: List[str]) -> int:
    wp_x, wp_y = WAYPOINT
    x, y = 0, 0
    for line in inp:
        action = line[0]
        amount = int(line[1:])
        if action == "F":
            x += wp_x * amount
            y += wp_y * amount
        elif action in {"R", "L"}:
            wp_x, wp_y = rotate(action, amount, [wp_x, wp_y])
        else:
            dx, dy = DIRECTIONS[action]
            wp_x += amount * dx
            wp_y += amount * dy
    return abs(x) + abs(y)


def main():
    with open(FILENAME) as f:
        inp = f.readlines()
        inp = [line.strip() for line in inp]
    print(f'Part 1: {part1(inp)}')
    print(f'Part 2: {part2(inp)}')


if __name__ == "__main__":
    main()
