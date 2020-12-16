#! /usr/bin/env python3
"""--- Advent of Code Day 16: Ticket Translation ---"""

from typing import List, Dict, Tuple
import re

FILENAME = "day_16.txt"

RE_FIELD = r"^([a-z ]+): (\d+-\d+) or (\d+-\d+)$"


def parse_input(inp: List[str]) -> List[str]:
    fields, my_ticket, nearby = inp
    field_ranges = {}
    for line in fields.split('\n'):
        match = re.search(RE_FIELD, line)
        field_name = match.groups()[0]
        ranges = []
        for m in match.groups()[1:]:
            lo, hi = m.split('-')
            ranges.append((int(lo), int(hi)))
        field_ranges[field_name] = ranges

    nearby = nearby.split('\n')[1:]
    nearby = [[int(x) for x in line.split(',')] for line in nearby]

    my_ticket = [int(x) for x in my_ticket.split('\n')[1].split(',')]

    return field_ranges, my_ticket, nearby


def part1(field_ranges: Dict[str, Tuple], nearby: List[List[int]]) -> Tuple[int, List[List[int]]]:
    error_rate = 0
    valid_tickets = []
    all_ranges = []
    for ranges in field_ranges.values():
        all_ranges.extend(ranges)

    for ticket in nearby:
        is_valid = True
        for num in ticket:
            if not any([num in range(lo, hi + 1) for lo, hi in all_ranges]):
                error_rate += num
                is_valid = False
        if is_valid:
            valid_tickets.append(ticket)

    return error_rate, valid_tickets


def part2(field_ranges: Dict[str, Tuple], my_ticket: List[int], valid_tickets: List[List[int]]) -> int:
    field_candidates = {i: set(field_ranges.keys())
                        for i in range(len(field_ranges))}
    for ticket in valid_tickets:
        for idx, num in enumerate(ticket):
            possible = set()
            for field, ranges in field_ranges.items():
                if any([num in range(lo, hi + 1) for lo, hi in ranges]):
                    possible.add(field)
            field_candidates[idx] &= possible

    while True:
        items = list(field_candidates.items())
        for idx, candidates in items:
            if type(candidates) == str:
                continue
            filtered = [cand for i, cand in items if i !=
                        idx and type(cand) != str]
            for field in candidates:
                if all([field not in s for s in filtered]):
                    field_candidates[idx] = field
                    break

        if all([type(v) == str for v in field_candidates.values()]):
            break

    res = 1
    for k, v in field_candidates.items():
        if "departure" in v:
            res *= my_ticket[k]

    return res


def main():
    with open(FILENAME) as f:
        inp = f.read().strip().split("\n\n")
    field_ranges, my_ticket, nearby = parse_input(inp)
    error_rate, valid_tickets = part1(field_ranges, nearby)
    print(f'Part 1: {error_rate}')
    print(f'Part 2: {part2(field_ranges, my_ticket, valid_tickets)}')


if __name__ == "__main__":
    main()
