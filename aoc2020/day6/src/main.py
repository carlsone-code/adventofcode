#!/usr/bin/env python
from adventofcode.aoc2020.helper_funcs import get_input


def part1(inp):
    groups = [set()]
    count = 0

    for line in inp:
        if line == '\n':
            count += len(groups[-1])
            groups.append(set())
            continue

        for ltr in line.strip():
            groups[-1].add(ltr)

    # count last group
    count += len(groups[-1])

    return count


def part2(inp):
    groups = [[]]
    count = 0
    group_size = 0

    for line in inp:
        if line == '\n':
            count = count_all(groups, group_size, count)
            group_size = 0
            groups.append([])
            continue

        group_size += 1

        for ltr in line.strip():
            groups[-1].append(ltr)

    # count last group
    count = count_all(groups, group_size, count)

    return count


def count_all(groups, group_size, count):
    uniq_ltrs = set(groups[-1])
    for ltr in uniq_ltrs:
        if groups[-1].count(ltr) == group_size:
            count += 1
    return count


if __name__ == '__main__':
    count = part1(get_input())
    print(f'Part1: The sum of the counts is {count}')

    count = part2(get_input())
    print(f'Part2: The sum of the counts is {count}')