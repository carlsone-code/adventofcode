#!/usr/bin/env python
from pprint import pprint
from adventofcode.aoc2020.helper_funcs import get_input


def part1(adapters):
    differences = {1: 0, 2:0, 3:1}  # 3-jolt diff starts w/ 1 for the device's built-in

    cur = 0
    for adp in adapters:
        if cur + 1 == adp:
            differences[1] += 1
        elif cur + 2 == adp:
            differences[2] += 1
        elif cur + 3 == adp:
            differences[3] += 1

        cur = adp

    return differences[1]*differences[3]


def part2(adapters):
    pass


if __name__ == '__main__':
    inp = sorted(int(n.strip()) for n in get_input())

    print(f'Part1: Product of 1-jolt differences and 3-jolt differences is {part1(inp)}')
    print(f'Part2: Number of distinct ways the adapters can be arraged is {part2(inp)}')