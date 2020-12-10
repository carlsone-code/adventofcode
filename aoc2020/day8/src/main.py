#!/usr/bin/env python
from adventofcode.aoc2020.helper_funcs import get_input


def get_instructions(inp, extra=False):
    instructions = []
    for line in inp:
        instructions.append([])
        instructions[-1] = [line.strip(), False]
        if extra:
            instructions[-1].append(False)
    
    return instructions


def part1(instructions):
    idx = 0
    acc = 0

    while True:
        if instructions[idx][1] is True:
            return acc

        cur = instructions[idx][0]
        instructions[idx][1] = True
        act, num = cur.split(' ')
        if act in 'acc':
            acc += int(num)
            idx += 1
        elif act == 'jmp':
            idx += int(num)
        elif act == 'nop':
            idx += 1


def part2(instructions):
    ret = False
    while ret is False:
        # Reset lines hit, but keep nops and jmps tried as True
        for instruct in instructions:
            instruct[1] = False
        ret, acc = traverse(instructions)

    return acc
    

def traverse(instructions):
    idx = 0
    acc = 0
    tried = False

    while True:
        if idx == len(instructions) or idx == len(instructions) + 1:
            return True, acc
        if instructions[idx][1] is True:
            return False, acc

        cur = instructions[idx][0]
        instructions[idx][1] = True
        act, num = cur.split(' ')
        if act in 'acc':
            acc += int(num)
            idx += 1
        elif act == 'jmp':
            if not tried and instructions[idx][2] == False:
                tried = True
                instructions[idx][2] = True
                # do nop
                idx += 1
            else:
                idx += int(num)
        elif act == 'nop':
            if not tried and instructions[idx][2] == False:
                tried = True
                instructions[idx][2] = True
                # do jmp
                idx += int(num)
            else:
                idx += 1


if __name__ == '__main__':

    acc = part1(get_instructions(get_input()))
    print(f'Part1: Value of accumulator at first inf loop: {acc}')

    acc = part2(get_instructions(get_input(), True))
    print(f'Part2: Value of accumulator at program termination: {acc}')