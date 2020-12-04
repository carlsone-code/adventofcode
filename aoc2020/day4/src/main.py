#!/usr/bin/env python
from adventofcode.aoc2020.helper_funcs import get_input


def part1(inp):
    passports = [[]]
    valid = invalid = 0

    for idx, line in enumerate(inp):
        kvps = line.strip().split(' ')
        for kvp in kvps:
            if kvp != '':
                key = kvp.split(':')[0]
                passports[-1].append(key)
        
        # Passport finished when newline or last line of input is encountered
        if line == '\n' or idx == len(inp) - 1:
            # check if passport has all required fields
            if all((k in passports[-1] for k in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'))):
                valid += 1
            else:
                invalid += 1

            # prepare next passport
            passports.append([])

    return valid, invalid


def part2(inp):
    passports = [{}]
    valid = 0

    for idx, line in enumerate(inp):
        kvps = line.strip().split(' ')
        for kvp in kvps:
            if kvp != '':
                key, value = kvp.split(':')
                passports[-1][key] = value

        # Passport finished when newline or last line of input is encountered
        if line == '\n' or idx == len(inp) - 1:
            # check if passport has all required fields and validate them
            while True:
                if not all((k in passports[-1] for k in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'))):
                    break

                byr = passports[-1]['byr']
                if not (byr.isdigit() and len(byr) == 4 and 1920 <= int(byr) <= 2002):
                    break

                iyr = passports[-1]['iyr']
                if not (iyr.isdigit() and len(iyr) == 4 and 2010 <= int(iyr) <= 2020):
                    break

                eyr = passports[-1]['eyr']
                if not (eyr.isdigit() and len(eyr) == 4 and 2020 <= int(eyr) <= 2030):
                    break

                hgt = passports[-1]['hgt']
                if not(hgt.endswith('cm') and 150 <= int(hgt[:-2]) <= 193
                        or hgt.endswith('in') and 59 <= int(hgt[:-2]) <= 76):
                    break

                hcl = passports[-1]['hcl']
                if not (hcl.startswith('#') and len(hcl[1:]) == 6 and
                        all(c in ('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f') for c in hcl[1:])):
                    break

                ecl = passports[-1]['ecl']
                if not (sum(col == ecl for col in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')) == 1):
                    break

                pid = passports[-1]['pid']
                if not (pid.isdigit() and len(pid) == 9):
                    break

                valid += 1
                break

            # prepare next passport
            passports.append({})

    return valid


if __name__ == '__main__':
    inp = get_input()
    valid, invalid = part1(inp)
    print(f'Part1: {valid}/{valid + invalid} passports are valid')

    valid = part2(inp)
    print(f'Part2: {valid} passports are valid')