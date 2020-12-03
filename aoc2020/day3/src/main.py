#!/usr/bin/env python
from adventofcode.aoc2020.helper_funcs import get_input, multiply_list

def main(inp, right_steps, down_steps):
    trees = 0
    col = 0
    row = 0
    line_length = len(inp[0])

    for _ in range(len(inp) - 1):
        col += right_steps
        row += down_steps

        # Sim line extension
        if col >= line_length:
            col -= line_length

        # Return if rows are exceeded when down_steps > 1
        if row > len(inp):
            return trees

        # Check spot for tree or snow
        if inp[row][col] == '#':
            trees += 1

    return trees


if __name__ == '__main__':
    inp = [line.strip() for line in get_input()]

    slopes = ((1,1), (3,1), (5,1), (7,1), (1,2))
    results = [] 
    for run, slope in enumerate(slopes):
        trees_hit = main(inp, *slope)
        results.append(trees_hit)
        run += 1
        print(f'Run {run} with a slope of {slope} hit {trees_hit} trees!')
    print(f'Product of trees hit across all runs = {multiply_list(results)}')
