#/usr/bin/env python
from adventofcode.aoc2020.helper_funcs import get_input


def main(inp):
    '''
    Return the number of valid passwords in the input given the following criteria:
        Format: #-# <letter>: <string of letters>
        Ex:     1-5 a: abkdjclccaa 
        Part1:  a must appear 1 to 5 times
        Result1: Pass
        Part2:  a must be in either position 1 or 5
        Result2: Pass
    '''
    valid1 = 0
    valid2 = 0
    for line in inp:
        # Parse the string into its components
        rang, ltr, string = line.strip().split(' ')
        low, high = (int(num) for num in rang.split('-'))
        ltr = ltr[0]

        # Part1
        if low <= int(string.count(ltr)) <= high:
            valid1 += 1

        # Part2
        # 'is not' and '!=' also work
        if bool(string[low - 1] == ltr) ^ bool(string[high - 1] == ltr):
            valid2 += 1

    return valid1, valid2

if __name__ == '__main__':
    valid1, valid2 = main(get_input())
    print(f'Part1: There are {valid1} valid passwords in the database')
    print(f'Part2: There are {valid2} valid passwords in the database')
