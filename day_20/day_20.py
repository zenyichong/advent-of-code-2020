#! /usr/bin/env python3
"""--- Advent of Code Day 20: Jurassic Jigsaw ---"""

from typing import List, Tuple, Set, Any
from collections import defaultdict
import numpy as np
from itertools import product

FILENAME = "day_20.txt"

SEA_MONSTER = ['                  # ',
               '#    ##    ##    ###',
               ' #  #  #  #  #  #   ']

tiles = dict()
id_to_edges = dict()
adjacent_tiles = defaultdict(set)
corners = set()


def get_edges(image: Any) -> List[Any]:  # "Any" in the type hints signify numpy arrays
    return [''.join(edge)
            for edge in [image[0], image[-1], image[:, 0], image[:, -1]]]


def parse_input(inp: List[str]) -> None:
    for tile in inp:
        tile_id, *image = tile.split('\n')
        tile_id = int(tile_id.strip(':').split()[1])
        image = np.array([list(row) for row in image])
        tiles[tile_id] = image

        edges = set()
        for edge in get_edges(image):
            edge = min(edge, edge[::-1])  # prevent reverse order edges showing up as duplicates
            edges.add(edge)

        id_to_edges[tile_id] = edges


def part1(inp: List[str]) -> int:
    prod = 1
    for id_1, e_1 in id_to_edges.items():
        common_edges = 0
        for id_2, e_2 in id_to_edges.items():
            if id_1 == id_2:
                continue

            if e_1 & e_2:
                adjacent_tiles[id_1].add(id_2)
                common_edges += 1

        if common_edges == 2:
            prod *= id_1
            corners.add(id_1)

    return prod


def get_neighbours(grid: List[List[int]], coord: Tuple[int, int]) -> List[Tuple[int, ...]]:
    grid_size = len(grid)
    res = []
    for dx, dy in {(-1, 0), (0, -1), (1, 0), (0, 1)}:
        x, y = coord[0] + dx, coord[1] + dy
        if (x in range(grid_size) and y in range(grid_size)) and grid[y][x]:
            res.append((grid[y][x], dx, dy))
    return res


def generate_orientations(tile: Any) -> List[Any]:
    orientations = []
    orig = tile.copy()
    flipped = np.fliplr(orig)
    for _ in range(4):
        orientations.append(orig)
        orientations.append(flipped)
        orig = np.rot90(orig)
        flipped = np.rot90(flipped)
    return orientations


def is_matching_edge(t_1: Any, t_2: Any, dx: int, dy: int) -> bool:
    if dx == -1:  # match right edge of t_1 with left edge of t_2
        return np.all(t_1[:, 0] == t_2[:, -1])

    elif dx == 1:  # match left edge of t_1 with right edge of t_2
        return np.all(t_1[:, -1] == t_2[:, 0])

    elif dy == -1:  # match top edge of t_1 with bottom edge of t_2
        return np.all(t_1[0] == t_2[-1])

    elif dy == 1:  # match bottom edge of t_1 with top edge of t_2
        return np.all(t_1[-1] == t_2[0])


def remove_borders(tile: Any):
    return tile[1:-1, 1:-1]


def count_monsters(image: List[str]) -> Tuple[bool, List[Tuple[int, int]]]:
    # Count the number of occurrence of monsters and returns a list of coordinates
    # if number of monsters > 0
    image_size = len(image)
    mon_length = len(SEA_MONSTER[0])
    mon_height = len(SEA_MONSTER)

    cnt = 0
    monster_coords = []
    for row in range(image_size):
        for col in range(image_size):
            monster_found = True
            opts = []
            for h in range(mon_height):
                for l in range(mon_length):
                    if (row + h not in range(image_size)) or (col + l not in range(image_size)):
                        monster_found = False
                        break

                    if SEA_MONSTER[h][l] == '#' and image[row + h][col + l] != '#':
                        monster_found = False
                        break
                    elif SEA_MONSTER[h][l] == '#' and image[row + h][col + l] == '#':
                        opts.append((col+l, row+h))
                if not monster_found:
                    break

            if monster_found:
                monster_coords.extend(opts)
                cnt += 1

    return cnt, monster_coords


def part2(inp: List[str]) -> int:
    grid_size = int(len(tiles) ** 0.5)
    grid = [[None for _ in range(grid_size)] for _ in range(grid_size)]
    grid_ids = [[None for _ in range(grid_size)] for _ in range(grid_size)]
    fixed_tiles = set()

    # Start off with a tile from the list of corners (doesn't matter which)
    # and it's adjacent tiles
    start = corners.pop()
    grid_ids[0][0] = start
    grid_ids[0][1], grid_ids[1][0] = adjacent_tiles[start]
    fixed_tiles.update([grid_ids[0][0], grid_ids[0][1], grid_ids[1][0]])
    while True:
        if len(fixed_tiles) == grid_size ** 2:
            break
        for j in range(grid_size):
            for i in range(grid_size):
                # Ignore if tile is already fixed
                if grid_ids[j][i]:
                    continue

                # Tiles that are fixed are removed from list of candidates
                candidates = set(tiles.keys()) - fixed_tiles

                # Find neighbours in the grid which are already fixed, then find
                # the set intersection of the adjacent tiles for each neighbour
                for nb, _, _ in get_neighbours(grid_ids, (i, j)):
                    candidates &= adjacent_tiles[nb]

                # Assume that only one possible candidate exists
                if len(candidates) == 1:
                    grid_ids[j][i] = list(candidates)[0]
                    fixed_tiles.add(grid_ids[j][i])

    for i in range(grid_size):
        for j in range(grid_size):
            curr_id = grid_ids[j][i]
            or_1 = generate_orientations(tiles[curr_id])

            # For all neighbours, find the orientations that have edges matching
            # the neighbour in that direction
            for nb, dx, dy in get_neighbours(grid_ids, (i, j)):
                candidates = []
                or_2 = generate_orientations(tiles[nb])
                for a, b in product(or_1, or_2):
                    if is_matching_edge(a, b, dx, dy):
                        candidates.append(a)

                # Keep only the orientations that belong in the list of candidates
                or_1 = [o for o in or_1 if any((o == c).all() for c in candidates)]

            # Assume that only one orientation is possible for each tile after comparing
            grid[j][i] = remove_borders(or_1[0])

    image = np.block(grid)
    for im in generate_orientations(image):
        cnt, monster_coords = count_monsters(im)
        if cnt > 0:
            for x, y in monster_coords:
                im[y][x] = 'O'
            im = [''.join(row) for row in im]
            # for row in im:
            #     print(row)
            water_roughness = ''.join(im).count('#')
            return water_roughness


def main():
    with open(FILENAME) as f:
        inp = f.read().strip().split("\n\n")
    parse_input(inp)
    print(f'Part 1: {part1(inp)}')
    print(f'Part 2: {part2(inp)}')


if __name__ == "__main__":
    main()
