'''Helper functions'''
import inspect


def get_input():
    path = inspect.stack()[1].filename.split('src')[0]
    input_file = f'{path}/input.txt'
    with open(input_file) as f:
        return f.readlines()


def multiply_list(values):
    '''Return product of all elements in a list.'''
    prod = 1
    for val in values:
        prod *= val
    return prod


