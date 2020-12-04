#! /usr/bin/env python3
"""--- Advent of Code Day 4: Passport Processing ---"""

import re
from typing import List

FILENAME = "day_04.txt"
REQUIRED = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

BYR_MIN = 1920
BYR_MAX = 2002
IYR_MIN = 2010
IYR_MAX = 2020
EYR_MIN = 2020
EYR_MAX = 2030
HGT_MIN_CM = 150
HGT_MAX_CM = 193
HGT_MIN_IN = 59
HGT_MAX_IN = 76
HCL_PAT = r"^#[0-9a-f]{6}$"
ECL = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
PID_PAT = r"^[0-9]{9}$"

passports = []


def part1(inp: List[str]) -> int:
    valid = 0
    for elem in inp:
        all_fields = [x.split(':') for x in elem.split()]
        all_fields = {x[0]: x[1] for x in all_fields}
        if all([field in all_fields for field in REQUIRED]):
            valid += 1
            passports.append(all_fields)
    return valid


def part2(inp: List[dict]) -> int:
    valid = 0
    for passport in inp:
        if not ((BYR_MIN <= int(passport["byr"]) <= BYR_MAX) and
                (IYR_MIN <= int(passport["iyr"]) <= IYR_MAX) and
                (EYR_MIN <= int(passport["eyr"]) <= EYR_MAX) and
                (re.match(HCL_PAT, passport["hcl"])) and
                (re.match(PID_PAT, passport["pid"])) and
                (passport["ecl"] in ECL)):
            continue

        height = int(re.findall(r"^[0-9]+", passport["hgt"])[0])
        if (passport["hgt"].endswith("cm")):
            if not (HGT_MIN_CM <= height <= HGT_MAX_CM):
                continue
        elif (passport["hgt"].endswith("in")):
            if not (HGT_MIN_IN <= height <= HGT_MAX_IN):
                continue
        else:
            continue
        valid += 1

    return valid


def main():
    with open(FILENAME) as f:
        inp = f.read().strip().split('\n\n')
    print(f'Part 1: {part1(inp)}')
    print(f'Part 2: {part2(passports)}')


if __name__ == "__main__":
    main()
