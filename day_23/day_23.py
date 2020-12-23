#! /usr/bin/env python3
"""--- Advent of Code Day 23: Crab Cups ---"""

from typing import List, Dict

FILENAME = "day_23.txt"


def move_cups(cups: Dict[int, int], cycles: int, start: int) -> Dict[int, int]:
    highest = max(cups)
    curr_cup = start
    for _ in range(cycles):
        picked = []
        tmp = curr_cup
        for _ in range(3):
            picked.append(cups[tmp])
            tmp = cups[tmp]

        dest = curr_cup - 1
        while dest in picked or dest == 0:
            dest -= 1
            if dest <= 0:
                dest = highest

        cups[curr_cup] = curr_cup = cups[picked[2]]
        cups[picked[2]] = cups[dest]
        cups[dest] = picked[0]

    return cups


def part1(inp: List[str]) -> str:
    inp = [int(x) for x in inp]
    cups = {inp[i]: inp[(i + 1) % len(inp)] for i in range(len(inp))}
    final_cups = move_cups(cups, 100, inp[0])

    labels = ""
    value = 1
    while final_cups[value] != 1:
        value = final_cups[value]
        labels += str(value)
    return labels


def part2(inp: List[str]) -> int:
    inp = [int(x) for x in inp]
    cups = inp + list(range(max(inp) + 1, 1_000_001))
    cups = {cups[i]: cups[(i + 1) % len(cups)] for i in range(len(cups))}
    final_cups = move_cups(cups, 10_000_000, inp[0])
    return final_cups[1] * final_cups[cups[1]]


def main():
    with open(FILENAME) as f:
        inp = f.read().strip()
    print(f'Part 1: {part1(inp)}')
    print(f'Part 2: {part2(inp)}')


if __name__ == "__main__":
    main()
