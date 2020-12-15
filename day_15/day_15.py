#! /usr/bin/env python3
"""--- Advent of Code Day 15: Rambunctious Recitation ---"""

from typing import List

FILENAME = "day_15.txt"


def sim_memory_game(start_nums: List[int], turns: int) -> int:
    nums_spoken = {num: idx for idx, num in enumerate(start_nums, 1)}
    curr = start_nums[-1]
    for i in range(len(start_nums), turns):
        prev = curr
        curr = i - nums_spoken.get(prev, i)
        nums_spoken[prev] = i
    return curr


def part1(inp: List[int]) -> int:
    turns = 2020
    return sim_memory_game(inp, turns)


def part2(inp: List[int]) -> int:
    turns = 30_000_000
    return sim_memory_game(inp, turns)


def main():
    with open(FILENAME) as f:
        inp = f.readlines()
        inp = [line.strip() for line in inp]
    start_nums = [int(x) for x in inp[0].split(',')]
    print(f'Part 1: {part1(start_nums)}')
    print(f'Part 2: {part2(start_nums)}')


if __name__ == "__main__":
    main()
