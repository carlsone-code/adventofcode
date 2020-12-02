#!/usr/bin/env python

def main(input_file, nums):
    print(f'Reading {input_file} for {nums} numbers that sum to 2020')

    with open(input_file) as f:
        lines = f.readlines()

    # Iterate through the list, summing current value to each value
    # left in list in search of 2020.
    # TODO implement recursion for any number of nums
    for idx, first in enumerate(lines):
        for second in lines[idx+1:]:
            for third in lines[idx+2:]:
                values = [int(first), int(second), int(third)]
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

    # TODO: need better way to locate input file. define root dir?
    input_file = 'input.txt'

    try:
        nums = int(sys.argv[1])
    except IndexError:
        print('Please supply the number of values to sum to 2020')
    except ValueError:
        print('Please give the number of values to sum to 2020 as a positive integer')
    else:
        main(input_file, nums)