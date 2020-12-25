#! /usr/bin/env python3
"""--- Advent of Code Day 25: Combo Breaker ---"""

from typing import List

FILENAME = "day_25.txt"


def get_loop_size(pub_key: int) -> int:
    value = 1
    loop_size = 0
    while value != pub_key:
        value *= 7
        value %= 20201227
        loop_size += 1

    return loop_size


def part1(inp: List[int]) -> int:
    pub_key_card, pub_key_door = inp
    loop_size_card = get_loop_size(pub_key_card)
    # loop_size_door = get_loop_size(pub_key_door)

    encryption_key_card = 1
    for _ in range(loop_size_card):
        encryption_key_card *= pub_key_door
        encryption_key_card %= 20201227

    # encryption_key_door = 1
    # for _ in range(loop_size_door):
    #     encryption_key_door *= pub_key_card
    #     encryption_key_door %= 20201227
    # assert encryption_key_card == encryption_key_door

    return encryption_key_card


def main():
    with open(FILENAME) as f:
        inp = f.readlines()
        inp = [int(line.strip()) for line in inp]
    print(f'Part 1: {part1(inp)}')


if __name__ == "__main__":
    main()
