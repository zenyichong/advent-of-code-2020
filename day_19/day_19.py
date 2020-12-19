#! /usr/bin/env python3
"""--- Advent of Code Day 19: Monster Messages  ---"""

from typing import List, Dict, Tuple, Union
import functools
from itertools import zip_longest
import re

FILENAME = "day_19.txt"


def parse_rules(inp: List[str]) -> Dict[int, Union[str, List[Tuple[int, ...]]]]:
    rules_dict = dict()
    for line in inp:
        n, rule = line.split(': ')
        rule = rule.strip('"').split()
        if rule[0] in {'a', 'b'}:
            rules_dict[int(n)] = rule[0]
        elif '|' in rule:
            idx = rule.index('|')
            sub_rule_1 = tuple([int(x) for x in rule[:idx]])
            sub_rule_2 = tuple([int(x) for x in rule[idx + 1:]])
            rules_dict[int(n)] = [sub_rule_1, sub_rule_2]
        else:
            sub_rule = tuple([int(x) for x in rule])
            rules_dict[int(n)] = [sub_rule]

    return rules_dict


def part1(inp: List[str]) -> int:
    rules, msgs = inp
    rules, msgs = rules.split('\n'), set(msgs.split('\n'))
    rules_dict = parse_rules(rules)

    # returns a list of possible patterns given a rule number
    @functools.lru_cache(None)
    def recurse(curr: int) -> List[str]:
        rule = rules_dict[curr]
        if type(rule) == str:
            return rule

        patterns = []
        for sub_rule in rule:
            sub_patterns = []
            for n in sub_rule:
                if not sub_patterns:
                    sub_patterns.extend(recurse(n))
                else:
                    sub_patterns = [s + res
                                    for s in sub_patterns
                                    for res in recurse(n)]
            patterns.extend(sub_patterns)

        return patterns

    valid_msgs = set(recurse(0))
    # main sub-rules that make up rule 0, returned for convenience in part 2
    rules_p2 = (recurse(42), recurse(31))

    return len(valid_msgs & msgs), rules_p2


def part2(inp: List[str], rules: Tuple[List[str], ...]) -> int:
    _, msgs = inp
    msgs = msgs.strip().split('\n')

    r_42, r_31 = rules
    segm_len = len(r_42[0])

    # makeshift regex to match each msg to the new rule 0 => (42 [42]+ 42 [42 31]+ 31)
    # which simplifies to ([42]+ [31]+)
    # x => matches r_42, y => matches r_31, z => matches neither
    regex = r"x+y+"
    total = 0
    for line in msgs:
        # split msg into lengths equal to the pattern length for r_42, r_31
        # Following assumptions hold:
        # - length of r_42 == length of r_31 == segm_len
        # - length of msgs is multiple of segm_len
        indices = [segm_len * i for i in range(len(line) // segm_len)]
        parts = [line[i:j] for i, j in zip_longest(indices, indices[1:])]

        tmp = ""
        for part in parts:
            if part in r_42:
                tmp += 'x'
            elif part in r_31:
                tmp += 'y'
            else:
                tmp += 'z'

        if tmp.count('x') > tmp.count('y') and re.fullmatch(regex, tmp):
            total += 1

    return total


def main():
    with open(FILENAME) as f:
        inp = f.read().split('\n\n')
    valid_p1, rules_p2 = part1(inp)
    print(f'Part 1: {valid_p1}')
    print(f'Part 2: {part2(inp, rules_p2)}')


if __name__ == "__main__":
    main()
