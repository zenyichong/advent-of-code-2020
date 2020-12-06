#! /usr/bin/env python3
"""--- Advent of Code Day 5: Binary Boarding ---"""

from typing import List, Tuple
import math

FILENAME = "day_05.txt"

BINARY_MAP = {'F': '0', 'B': '1', 'L': '0', 'R': '1'}


def get_seat_id(seat: str) -> Tuple[int, int]:
    seat_location = ''.join([BINARY_MAP[c] for c in seat])
    row = int(seat_location[:7], 2)
    col = int(seat_location[7:], 2)
    seat_id = row * 8 + col
    return seat_id


def part1(inp: List[str]) -> int:
    max_seat_id = 0
    for seat in inp:
        seat_id = get_seat_id(seat)
        if seat_id > max_seat_id:
            max_seat_id = seat_id
    return max_seat_id


def part2(inp: List[str], max_seat_id: int) -> int:
    max_row = math.ceil((max_seat_id - 8) / 8)
    all_seat_ids = set(range(max_row * 8 + 8))
    for seat in inp:
        seat_id = get_seat_id(seat)
        all_seat_ids.remove(seat_id)

    for remaining in all_seat_ids:
        if ((remaining - 1) not in all_seat_ids) and ((remaining + 1) not in all_seat_ids):
            return remaining


def main():
    with open(FILENAME) as f:
        inp = f.readlines()
        inp = [line.strip() for line in inp]
    max_seat_id = part1(inp)
    print(f'Part 1: {max_seat_id}')
    print(f'Part 2: {part2(inp, max_seat_id)}')


if __name__ == "__main__":
    main()
