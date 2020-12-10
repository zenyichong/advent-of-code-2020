#! /usr/bin/env python3
"""--- Advent of Code Day 10: Adapter Array ---"""

from typing import List
from collections import Counter
import functools

FILENAME = "day_10.txt"


def part1(inp: List[int]) -> int:
    diff = []
    for i in range(1, len(inp)):
        diff.append(inp[i] - inp[i - 1])
    counter = Counter(diff)
    return counter[1] * counter[3]


def part2(inp: List[int]) -> int:

    @functools.lru_cache(64)
    def find_arrangements(idx: int) -> int:
        if idx == len(inp) - 1:
            return 1
        arrangements = 0
        for i in range(idx + 1, len(inp)):
            if inp[i] - inp[idx] <= 3:
                arrangements += find_arrangements(i)
            else:
                break
        return arrangements

    return find_arrangements(0)


def main():
    with open(FILENAME) as f:
        inp = f.readlines()
        inp = [int(line.strip()) for line in inp]
    inp.append(0)
    inp.sort()
    inp.append(inp[-1] + 3)
    print(f'Part 1: {part1(inp)}')
    print(f'Part 2: {part2(inp)}')


if __name__ == "__main__":
    main()
