#!/usr/bin/env python
from adventofcode.aoc2020.input_template import get_input

def main(inp, nums):
    '''
    Iterate through the input, summing current value to each value
    left in list in search of 2020.
    '''
    # TODO implement recursion for any number of nums
    for idx, first in enumerate(inp):
        for second in inp[idx+1:]:
            for third in inp[idx+2:]:
                values = [first, second, third]
                if sum(values) == 2020:
                    print(f'FOUND: {values}')
                    print(f'ANSWER = {multiply_list(values)}')
                    return
    print(f'No {nums} numbers were found that sum to 2020')

def multiply_list(values):
    '''Return product of all elements in a list.'''
    prod = 1
    for val in values:
        prod *= val
    return prod

if __name__ == '__main__':
    import sys

    inp = [int(line) for line in get_input()]

    try:
        nums = int(sys.argv[1])
    except IndexError:
        print('Please supply the number of values to sum to 2020')
    except ValueError:
        print('Please give the number of values to sum to 2020 as a positive integer')
    else:
        main(inp, nums)