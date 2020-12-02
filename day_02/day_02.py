#! /usr/bin/env python3
"""--- Advent of Code Day 2: Password Philosophy ---"""

from typing import List
from collections import Counter

FILENAME = "day_02.txt"


def part1(inp: List[str]) -> int:
    inp = [tuple(line.split()) for line in inp]
    valid = 0
    for elem in inp:
        policy, letter, password = elem
        lo, hi = [int(num) for num in policy.split('-')]
        counts = Counter(password)
        num_occurences = counts.get(letter.strip(':'))
        if (num_occurences is not None) and (lo <= num_occurences <= hi):
            valid += 1
    return valid


def part2(inp: List[str]) -> int:
    inp = [tuple(line.split()) for line in inp]
    valid = 0
    for elem in inp:
        policy, letter, password = elem
        idx1, idx2 = [int(num) for num in policy.split('-')]
        letter = letter.strip(':')
        if (password[idx1 - 1] == letter) ^ (password[idx2 - 1] == letter):
            valid += 1
    return valid


def main():
    with open(FILENAME) as f:
        inp = f.readlines()
        inp = [line.strip() for line in inp]
    print(f'Part 1: {part1(inp)}')
    print(f'Part 2: {part2(inp)}')


if __name__ == "__main__":
    main()
