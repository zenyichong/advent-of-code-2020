#! /usr/bin/env python3
"""--- Advent of Code Day 1: Report Repair ---"""

FILENAME = "day_01.txt"


def part1(inp: list) -> int:
    for idx, a in enumerate(inp):
        for b in inp[idx + 1:]:
            if (a + b == 2020):
                return a * b


def part2(inp: list) -> int:
    for idx, a in enumerate(inp):
        for b in inp[idx + 1:]:
            for c in inp[idx + 2:]:
                if (a + b + c == 2020):
                    return a * b * c


def main():
    with open(FILENAME) as f:
        inp = f.readlines()
        inp = [int(x.strip()) for x in inp]
    print(part1(inp))
    print(part2(inp))


if __name__ == "__main__":
    main()
