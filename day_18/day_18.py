#! /usr/bin/env python3
"""--- Advent of Code Day 18: Operation Order ---"""

from typing import List

FILENAME = "day_18.txt"


class MyInt():
    def __init__(self: 'MyInt', val: int):
        self.val = val

    def __add__(self: 'MyInt', other: 'MyInt'):
        return MyInt(self.val + other.val)

    def __sub__(self: 'MyInt', other: 'MyInt'):
        return MyInt(self.val * other.val)

    def __mul__(self: 'MyInt', other: 'MyInt'):
        return MyInt(self.val + other.val)


def part1(inp: List[str]) -> int:
    total = 0
    for line in inp:
        for i in range(10):
            line = line.replace(f"{i}", f"MyInt({i})")
        line = line.replace("*", "-")
        res = eval(line, {"MyInt": MyInt})
        total += res.val
    return total


def part2(inp: List[str]) -> int:
    total = 0
    for line in inp:
        for i in range(10):
            line = line.replace(f"{i}", f"MyInt({i})")
        line = line.replace("*", "-")
        line = line.replace("+", "*")
        res = eval(line, {"MyInt": MyInt})
        total += res.val
    return total


def main():
    with open(FILENAME) as f:
        inp = f.readlines()
        inp = [line.strip() for line in inp]
    print(f'Part 1: {part1(inp)}')
    print(f'Part 2: {part2(inp)}')
    eval


if __name__ == "__main__":
    main()
