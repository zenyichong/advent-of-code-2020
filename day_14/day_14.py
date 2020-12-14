#! /usr/bin/env python3
"""--- Advent of Code Day 14: Docking Data ---"""

from typing import List, Tuple, Union
import re

FILENAME = "day_14.txt"

RE_MASK = r"^mask = (\w+)$"
RE_MEM = r"^mem\[(\d+)\] = (\d+)$"
NUM_BITS = 36


def parse_input(line: str) -> Tuple[str, Union[str, Tuple[str, str]]]:
    match = re.fullmatch(RE_MASK, line)
    if match:
        return "mask", match.groups()[0]
    match = re.search(RE_MEM, line)
    return "mem", match.groups()


def part1(inp: List[str]) -> int:
    mem = dict()
    mask = ""
    for line in inp:
        match = parse_input(line)
        if match[0] == "mask":
            mask = match[1]
            continue
        elif match[0] == "mem":
            addr, val = match[1]

        # Converts to decimal to binary, then pads with zeros until it reaches
        # a length of NUM_BITS, finally turning into a list for mutability
        val = list(bin(int(val))[2:].zfill(NUM_BITS))
        # Overwrite written value bit if bitmask is 0 or 1 / not X
        for idx, bit in enumerate(list(mask)):
            if bit != 'X':
                val[idx] = bit
        mem[int(addr)] = int((''.join(val)), 2)
    return sum(mem.values())


def part2(inp: List[str]) -> int:
    mem = dict()
    mask = ""
    for line in inp:
        match = parse_input(line)
        if match[0] == "mask":
            mask = match[1]
            continue
        elif match[0] == "mem":
            addr, val = match[1]

        addr = list(bin(int(addr))[2:].zfill(NUM_BITS))
        # If bit is 1, overwrite corresponding memory address bit with 1
        for idx, bit in enumerate(list(mask)):
            if bit == '1':
                addr[idx] = bit

        addresses = [addr]
        # Obtain all possible combinations of bits when bitmask bit is X
        for idx, bit in enumerate(list(mask)):
            if bit == 'X':
                tmp = []
                for item in addresses:
                    item = list(item)
                    item[idx] = '0'
                    tmp.append(''.join(item))
                    item[idx] = '1'
                    tmp.append(''.join(item))
                addresses = tmp
        for addr in addresses:
            mem[int(addr, 2)] = int(val)
    return sum(mem.values())


def main():
    with open(FILENAME) as f:
        inp = f.readlines()
        inp = [line.strip() for line in inp]
    print(f'Part 1: {part1(inp)}')
    print(f'Part 2: {part2(inp)}')


if __name__ == "__main__":
    main()
