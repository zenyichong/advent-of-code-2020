#! /usr/bin/env python3
"""--- Advent of Code Day 22: Crab Combat ---"""

from typing import List, Deque, Tuple
from collections import deque
from itertools import islice

FILENAME = "day_22.txt"


def calculate_score(cards: Deque[int]) -> int:
    score = 0
    for i, n in enumerate(reversed(cards), 1):
        score += i * n
    return score


def part1(inp: List[str]) -> int:
    player_1, player_2 = inp
    player_1 = deque([int(x) for x in player_1.split('\n')[1:]])
    player_2 = deque([int(x) for x in player_2.split('\n')[1:]])

    while player_1 and player_2:
        card_1 = player_1.popleft()
        card_2 = player_2.popleft()
        if card_1 > card_2:
            player_1.append(card_1)
            player_1.append(card_2)
        else:
            player_2.append(card_2)
            player_2.append(card_1)

    if player_1:
        return calculate_score(player_1)
    else:
        return calculate_score(player_2)


def get_round_hash(player_1: Deque[int], player_2: Deque[int]) -> str:
    hash = "p1"
    for card in player_1:
        hash += ','
        hash += str(card)
    hash += "p2"
    for card in player_2:
        hash += ','
        hash += str(card)
    return hash


def recursive_combat(player_1: Deque[int], player_2: Deque[int]) -> Tuple[Deque[int], ...]:
    history = set()
    player_1, player_2 = deque(player_1), deque(player_2)
    while player_1 and player_2:
        # Hashes the current round's cards and checks if the exact same round
        # has been played before
        curr_hash = get_round_hash(player_1, player_2)
        if curr_hash in history:
            return player_1, deque()
        history.add(curr_hash)

        card_1 = player_1.popleft()
        card_2 = player_2.popleft()
        # if both player hands have at least as many cards as most recent card drawn
        # enter recursive combat
        if len(player_1) >= card_1 and len(player_2) >= card_2:
            tmp_1, tmp_2 = recursive_combat(islice(player_1, card_1), islice(player_2, card_2))
            if tmp_1:
                player_1.append(card_1)
                player_1.append(card_2)
            elif tmp_2:
                player_2.append(card_2)
                player_2.append(card_1)
        # else regular rules apply
        else:
            if card_1 > card_2:
                player_1.append(card_1)
                player_1.append(card_2)
            else:
                player_2.append(card_2)
                player_2.append(card_1)

    return player_1, player_2


def part2(inp: List[str]) -> int:
    player_1, player_2 = inp
    player_1 = [int(x) for x in player_1.split('\n')[1:]]
    player_2 = [int(x) for x in player_2.split('\n')[1:]]

    player_1, player_2 = recursive_combat(player_1, player_2)

    if player_1:
        return calculate_score(player_1)
    else:
        return calculate_score(player_2)


def main():
    with open(FILENAME) as f:
        inp = f.read().strip().split('\n\n')
    print(f'Part 1: {part1(inp)}')
    print(f'Part 2: {part2(inp)}')


if __name__ == "__main__":
    main()
