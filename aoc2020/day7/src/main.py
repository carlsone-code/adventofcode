#!/usr/bin/env python
from adventofcode.aoc2020.helper_funcs import get_input


def create_bags(inp):
    bags = {}

    for line in inp:
        split_line = line.split('bags contain')
        otr_bag = split_line[0].strip()
        bags[otr_bag] = {}

        inr_bags_line = split_line[1].strip()
        for _ in range(inr_bags_line.count('bag')):
            if 'no' in inr_bags_line:
                bags[otr_bag] = {}
                continue

            inr_bag_line = inr_bags_line.split('bags')[0].strip().split(' ')
            num = int(inr_bag_line[0])
            inr_bag = ' '.join([inr_bag_line[1], inr_bag_line[2]])

            bags[otr_bag][inr_bag] = num

            if ',' in inr_bags_line:
                inr_bags_line = inr_bags_line[inr_bags_line.index(',') + 1:].strip()

    return bags

def part1(bags):
    count = 0
    for bag in bags:
        if contains_shiny(bag, bags):
            count += 1
    return count


def contains_shiny(bag, bags):
    for inr_bag in bags[bag].keys():
        if inr_bag == 'shiny gold' or contains_shiny(inr_bag, bags):
            return True
    return False


def part2(bags):
    return count_bags('shiny gold', bags)


def count_bags(bag, bags):
    count = 0
    for inr_bag, num in bags[bag].items():
        count += num + num*count_bags(inr_bag, bags)
    return count


if __name__ == '__main__':
    bags = create_bags(get_input())

    count = part1(bags)
    print(f'Part1: How many bag colors can eventually contain at least one shiny gold bag? {count}')

    count = part2(bags)
    print(f'Part2: How many individual bags are required inside your single shiny gold bag? {count}')