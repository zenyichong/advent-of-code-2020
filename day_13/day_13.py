#! /usr/bin/env python3
"""--- Advent of Code Day 13: Shuttle Search ---"""

from typing import List
import math

FILENAME = "day_13.txt"


def part1(inp: List[str]) -> int:
    earliest = int(inp[0])
    bus_ids = [int(elem) for elem in inp[1].split(',') if elem != 'x']
    min_waiting_time = float("inf")
    chosen_bus = -1
    for bus in bus_ids:
        waiting_time = bus * math.ceil(earliest / bus) - earliest
        if waiting_time < min_waiting_time:
            min_waiting_time = waiting_time
            chosen_bus = bus
    return chosen_bus * min_waiting_time


def part2(inp: List[str]) -> int:
    schedule = [(int(bus_id), idx)
                for idx, bus_id in enumerate(inp[1].split(','))
                if bus_id != 'x']

    timestamp = schedule[0][0]
    n = timestamp
    for bus_id, offset in schedule[1:]:
        while True:
            if (timestamp + offset) % bus_id == 0:
                n *= bus_id
                break
            timestamp += n
    return timestamp


def main():
    with open(FILENAME) as f:
        inp = f.readlines()
        inp = [line.strip() for line in inp]
    print(f'Part 1: {part1(inp)}')
    print(f'Part 2: {part2(inp)}')


if __name__ == "__main__":
    main()
