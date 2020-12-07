#!/usr/bin/env python
from adventofcode.aoc2020.helper_funcs import get_input
from pprint import pprint


def main(inp):
    boarding_passes = {} 

    for line in inp:
        line = line.strip()
        row_string, column_string = line[:7], line[7:]

        # calc row
        row = get_num(row_string, 'F', 'B', 0, 2**(len(row_string)) - 1)

        # calc column
        column = get_num(column_string, 'L', 'R', 0, 2**(len(column_string)) - 1)

        # calc ID
        boarding_passes[line] = row*8 + column

    i = 0
    # lowest id is 0
    # highest id i 1023
    ids = boarding_passes.values()
    while i < 1040:
        if i not in ids:
            print(f'{i} not in ids')
        i += 1
    
    return max(boarding_passes.values())


def get_num(s, slwr, supr, lwr, upr):
    # get final letter
    if len(s) == 1:
        if s == slwr:
            return lwr
        return upr

    if s[0] == slwr:
        upr -= round((upr - lwr)/2)
    elif s[0] == supr:
        lwr += round((upr - lwr)/2)

    return get_num(s[1:], slwr, supr, lwr, upr)


if __name__ == '__main__':
    highest_id = main(get_input())
    print(f'Part1: The highest seat ID is {highest_id}')