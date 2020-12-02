#!/usr/bin/env python

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

    # TODO: need better way to locate input file. define root dir?
    input_file = 'input.txt'
    with open(input_file) as f:
        lines = f.readlines()
        inp = [int(line) for line in lines]

    try:
        nums = int(sys.argv[1])
    except IndexError:
        print('Please supply the number of values to sum to 2020')
    except ValueError:
        print('Please give the number of values to sum to 2020 as a positive integer')
    else:
        main(inp, nums)