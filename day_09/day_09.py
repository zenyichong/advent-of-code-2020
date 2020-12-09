#! /usr/bin/env python3
"""--- Advent of Code Day 9: Encoding Error ---"""

from typing import List

FILENAME = "day_09.txt"
PREAMBLE = 25


def is_valid_num(inp: List[int], num: int) -> bool:
    for idx, a in enumerate(inp):
        for b in inp[idx + 1:]:
            if (a + b == num):
                return True
    return False


def part1(inp: List[int]) -> int:
    for i in range(PREAMBLE, len(inp)):
        if not is_valid_num(inp[i - PREAMBLE:i], inp[i]):
            return inp[i]


def part2(inp: List[int], num: int) -> int:
    for i in range(len(inp)):
        start = i
        end = len(inp)
        total = inp[i]
        found = False
        for j in range(i + 1, len(inp)):
            total += inp[j]
            if total == num:
                end = j
                found = True
                break
            elif total > num:
                break
        if found:
            break

    return (min(inp[start:end + 1]) + max(inp[start:end + 1]))


def main():
    with open(FILENAME) as f:
        inp = f.readlines()
        inp = [int(line.strip()) for line in inp]
    invalid_num = part1(inp)
    print(f'Part 1: {invalid_num}')
    print(f'Part 2: {part2(inp, invalid_num)}')


if __name__ == "__main__":
    main()
