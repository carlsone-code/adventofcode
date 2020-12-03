'''Helper functions'''


def get_input():
    # TODO: need better way to locate input file. define root dir?
    input_file = 'input.txt'
    with open(input_file) as f:
        return f.readlines()


def multiply_list(values):
    '''Return product of all elements in a list.'''
    prod = 1
    for val in values:
        prod *= val
    return prod


