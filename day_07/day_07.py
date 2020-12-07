#! /usr/bin/env python3
"""--- Advent of Code Day 7: Handy Haversacks ---"""

from typing import List
from collections import defaultdict
import re
import functools

FILENAME = "day_07.txt"

TARGET = "shiny gold"
bags = defaultdict(list)


def parse_input(inp: List[str]) -> None:
    outer = r"^([a-z ]*?) bag"
    inner = r"(\d) ([a-z ]*?) bags?[.,]"
    for line in inp:
        outer_bag = re.findall(outer, line)[0]
        inner_bags = re.findall(inner, line)
        for amount, bag in inner_bags:
            bags[outer_bag].append((int(amount), bag))


@functools.lru_cache(64)
def recursive_find(colour: str) -> bool:
    for _, bag in bags[colour]:
        if (bag == TARGET) or (recursive_find(bag)):
            return True
    return False


@functools.lru_cache(64)
def recursive_add(colour: str) -> int:
    total = 0
    for amount, bag in bags[colour]:
        total += amount
        total += amount * recursive_add(bag)
    return total


def part1() -> int:
    total = 0
    for colour in list(bags.keys()):
        if recursive_find(colour):
            total += 1
    return total


def part2() -> int:
    return recursive_add(TARGET)


def main():
    with open(FILENAME) as f:
        inp = f.readlines()
        inp = [line.strip() for line in inp]
    parse_input(inp)
    print(f'Part 1: {part1()}')
    print(f'Part 2: {part2()}')


if __name__ == "__main__":
    main()
