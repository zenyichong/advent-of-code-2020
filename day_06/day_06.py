#! /usr/bin/env python3
"""--- Advent of Code Day 6: Custom Customs ---"""

from typing import List

FILENAME = "day_06.txt"


def part1(inp: List[str]) -> int:
    answers = [item.split() for item in inp]
    count = 0
    for group in answers:
        count += len(set(''.join(group)))
    return count


def part2(inp: List[str]) -> int:
    answers = [item.split() for item in inp]
    count = 0
    for group in answers:
        group = [set(yes) for yes in group]
        count += len(set.intersection(*group))
    return count


def main():
    with open(FILENAME) as f:
        inp = f.read().strip().split("\n\n")
    print(f'Part 1: {part1(inp)}')
    print(f'Part 2: {part2(inp)}')


if __name__ == "__main__":
    main()
