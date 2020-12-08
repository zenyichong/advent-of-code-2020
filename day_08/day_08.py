#! /usr/bin/env python3
"""--- Advent of Code Day 8: Handheld Halting ---"""

from typing import List, Tuple

FILENAME = "day_08.txt"


def execute(inp: List[Tuple[str, int]]) -> Tuple[bool, int]:
    pointer = 0
    acc = 0
    visited = set()
    terminates = False
    num_instructions = len(inp)
    while True:
        if pointer in visited:
            break
        elif pointer == num_instructions:
            terminates = True
            break
        visited.add(pointer)
        op, cnt = inp[pointer]
        if op == "nop":
            pointer += 1
        elif op == "acc":
            acc += cnt
            pointer += 1
        elif op == "jmp":
            pointer += cnt

    return terminates, acc


def part1(inp: List[Tuple[str, int]]) -> int:
    _, acc = execute(inp)
    return acc


def part2(inp: List[Tuple[str, int]]) -> int:
    for i in range(len(inp)):
        tmp = inp[i][0]
        if tmp == "nop":
            inp[i][0] = "jmp"
        elif tmp == "jmp":
            inp[i][0] = "nop"
        else:
            continue
        terminates, acc = execute(inp)
        inp[i][0] = tmp
        if terminates:
            return acc


def main():
    with open(FILENAME) as f:
        inp = f.readlines()
        inp = [line.strip().split() for line in inp]
        inp = [[line[0], int(line[1])] for line in inp]
    print(f'Part 1: {part1(inp)}')
    print(f'Part 2: {part2(inp)}')


if __name__ == "__main__":
    main()
