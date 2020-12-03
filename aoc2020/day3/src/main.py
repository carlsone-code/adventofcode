#!/usr/bin/env python
from adventofcode.aoc2020.helper_funcs import get_input, multiply_list

def main(inp, slope):
    trees = 0
    col = 0
    row = 0
    line_length = len(inp[0])

    for _ in range(len(inp) - 1):
        # Move the slope. Slope is right 3, down 1
        col += slope[0]
        row += slope[1]

        # Catch if rows are exceeded when moving down is > 1
        if row > len(inp):
            return trees

        # Check character for tree or snow
        try:
            tree = check_for_tree(inp, row, col)
        except IndexError:
            # move index back to start of line 
            col -= line_length
            tree = check_for_tree(inp, row, col)

        if tree:
            trees += 1

    return trees

def check_for_tree(inp, row, col):
    if inp[row][col] == '#':
        return True
    return False


if __name__ == '__main__':
    inp = [line.strip() for line in get_input()]

    slopes = ((1,1), (3,1), (5,1), (7,1), (1,2))
    results = [] 
    for run, slope in enumerate(slopes):
        trees_hit = main(inp, slope)
        results.append(trees_hit)
        run += 1
        print(f'Run {run} with a slope of {slope} hit {trees_hit} trees!')
    print(f'Product of trees hit across all runs = {multiply_list(results)}')
