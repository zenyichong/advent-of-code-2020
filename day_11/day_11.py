#! /usr/bin/env python3
"""--- Advent of Code Day 11: Seating System ---"""

from typing import List, Tuple
from copy import copy

FILENAME = "day_11.txt"
FLOOR = '.'
EMPTY = 'L'
OCCUPIED = '#'
directions = [(x, y) for x in {-1, 0, 1}
              for y in {-1, 0, 1}
              if (x != 0 or y != 0)]


def get_adjacent_seats(inp: List[str], coord: Tuple[int, int]) -> List[str]:
    res = []
    for dx, dy in directions:
        x, y = coord[0] + dx, coord[1] + dy
        if (x in range(len(inp[0]))) and (y in range(len(inp))):
            res.append(inp[y][x])
    return res


def get_first_seats_seen(inp: List[str], coord: Tuple[int, int]) -> List[str]:
    res = []
    for dx, dy in directions:
        x, y = coord
        while True:
            x += dx
            y += dy
            if (x not in range(len(inp[0]))) or (y not in range(len(inp))):
                break
            if (inp[y][x] == FLOOR):
                continue
            res.append(inp[y][x])
            break
    return res


def simulate_cycle(inp: List[str], is_part1: bool) -> List[str]:
    new = []
    max_adjacent = 4 if is_part1 else 5
    for y in range(len(inp)):
        row = ''
        for x in range(len(inp[0])):
            seat = inp[y][x]
            if is_part1:
                adjacent_seats = get_adjacent_seats(inp, (x, y))
            else:
                adjacent_seats = get_first_seats_seen(inp, (x, y))
            if (seat == EMPTY) and (OCCUPIED not in adjacent_seats):
                row += OCCUPIED
            elif (seat == OCCUPIED) and (adjacent_seats.count(OCCUPIED) >= max_adjacent):
                row += EMPTY
            else:
                row += seat
        new.append(row)
    return new


def part1(inp: List[str]) -> int:
    curr = copy(inp)
    while True:
        new = simulate_cycle(curr, True)
        if curr == new:
            break
        curr = new
    return ''.join(new).count(OCCUPIED)


def part2(inp: List[str]) -> int:
    curr = copy(inp)
    while True:
        new = simulate_cycle(curr, False)
        if curr == new:
            break
        curr = new
    return ''.join(new).count(OCCUPIED)


def main():
    with open(FILENAME) as f:
        inp = f.readlines()
        inp = [line.strip() for line in inp]
    print(f'Part 1: {part1(inp)}')
    print(f'Part 2: {part2(inp)}')


if __name__ == "__main__":
    main()
