#! /usr/bin/env python3
"""--- Advent of Code Day 3: Toboggan Trajectory ---"""

from typing import List

FILENAME = "day_03.txt"
TREE = '#'
EMPTY = '.'


def part1(inp: List[str]) -> int:
    row_len = len(inp[0])
    x = 0
    num_trees = 0
    for row in inp:
        if row[x % row_len] == TREE:
            num_trees += 1
        x += 3
    return num_trees


def part2(inp: List[str]) -> int:
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    row_len = len(inp[0])
    res = 1
    for right, down in slopes:
        x = right
        num_trees = 0
        for row in inp[down::down]:
            if row[x % row_len] == TREE:
                num_trees += 1
            x += right
        res *= num_trees
    return res


def main():
    with open(FILENAME) as f:
        inp = f.readlines()
        inp = [line.strip() for line in inp]
    print(f'Part 1: {part1(inp)}')
    print(f'Part 2: {part2(inp)}')


if __name__ == "__main__":
    main()
