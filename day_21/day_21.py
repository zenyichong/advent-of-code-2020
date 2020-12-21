#! /usr/bin/env python3
"""--- Advent of Code Day 21: Allergen Assessment ---"""

from typing import List, Dict, Tuple
from collections import defaultdict
import re

FILENAME = "day_21.txt"


def part1(inp: List[str]) -> Tuple[int, Dict[str, set]]:
    pattern = r"^(.*) \(contains (.*)\)$"
    allergen_dict = defaultdict(list)
    foods = []
    ingredients_w_allergens = set()

    for line in inp:
        match = re.fullmatch(pattern, line)
        ingredients, allergens = match.groups()
        ingredients, allergens = ingredients.split(), allergens.split(", ")
        foods.append(ingredients)
        for al in allergens:
            allergen_dict[al].append(set(ingredients))

    for al in allergen_dict:
        possible = set.intersection(*allergen_dict[al])
        allergen_dict[al] = possible
        ingredients_w_allergens.update(possible)

    total = 0
    for food in foods:
        for ing in food:
            if ing not in ingredients_w_allergens:
                total += 1

    return total, allergen_dict


def part2(allergen_dict: Dict[str, set]) -> int:
    while True:
        items = allergen_dict.items()
        for allergen, ingredients in items:
            if type(ingredients) == str:
                continue

            if len(ingredients) == 1:
                ingredient = list(ingredients)[0]
                allergen_dict[allergen] = ingredient
                for al, _ in items:
                    if allergen != al and type(allergen_dict[al]) == set:
                        try:
                            allergen_dict[al].remove(ingredient)
                        except KeyError:
                            pass

        if all([type(ing) == str for ing in allergen_dict.values()]):
            break

    ing_list = ','.join([v for k, v in sorted(allergen_dict.items(), key=lambda x: x[0])])
    return ing_list


def main():
    with open(FILENAME) as f:
        inp = f.readlines()
        inp = [line.strip() for line in inp]
    ans_p1, allergen_dict = part1(inp)
    print(f'Part 1: {ans_p1}')
    print(f'Part 2: {part2(allergen_dict)}')


if __name__ == "__main__":
    main()
