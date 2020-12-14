#!/usr/bin/env python
from adventofcode.aoc2020.helper_funcs import get_input


def part1(inp):
    sidx = 0
    eidx = 25
    for num in inp[eidx:]:
        preamble = [num for num in inp[sidx:eidx]]

        found = False
        while found is False:
            for first in preamble:
                for second in preamble:
                    if first == second:
                        continue

                    if first + second == num:
                        # print(f'{first} + {second} == {num}')
                        found = True
            if found is False:
                return num

        sidx += 1
        eidx += 1


def part2(inp, p1):
    for idx in range(len(inp)):
        cur = 1
        contiguous = []
        while sum(contiguous) < p1:
            contiguous = inp[idx:idx+cur]
            cur += 1
        if sum(contiguous) == p1:
            return contiguous


if __name__ == '__main__':
    inp = [int(num.strip()) for num in get_input()]

    num = part1(inp)
    print(f'Part1: No pair of numbers sum to {num}')

    contiguous = part2(inp, num)
    print(f'Part2: The encryption weakness is {min(contiguous) + max(contiguous)}')