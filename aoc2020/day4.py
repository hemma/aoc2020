# https://adventofcode.com/2020/day/4
import re


def height_rule(x: str) -> bool:
    if 'in' in x:
        height = x.split('in')[0]
        try:
            height = int(height)
            return 59 <= height <= 76
        except ValueError:
            return False
    if 'cm' in x:
        height = x.split('cm')[0]
        try:
            height = int(height)
            return 150 <= height <= 193
        except ValueError:
            return False

    return False


pattern = '^a...s$'
test_string = 'abyss'
result = re.match(pattern, test_string)

PASSPORT_RULES_PART_TWO = {'byr': lambda x: 1920 <= int(x) <= 2002,
                           'iyr': lambda x: 2010 <= int(x) <= 2020,
                           'eyr': lambda x: 2020 <= int(x) <= 2030,
                           'hgt': height_rule, 'hcl': lambda x: re.match('^#[0-9a-f]{6}$', x),
                           'ecl': lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
                           'pid': lambda x: x.isdigit() and len(x) == 9}

REQUIRED_KEYS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def is_valid_passport(passport: dict) -> bool:
    for key in REQUIRED_KEYS:
        if key not in passport:
            return False

    return True


def is_valid_passport_part_two(passport: dict) -> bool:
    if not is_valid_passport(passport):
        return False
    for key, rule_func in PASSPORT_RULES_PART_TWO.items():
        try:
            if not rule_func(passport[key].strip()):
                return False
        except ValueError:
            return False

    return True


def split_to_passports(lines: list[str]) -> list[dict]:
    passports = []
    current_passport = {}
    for line in lines:
        if len(line.strip()) == 0:
            passports.append(current_passport)
            current_passport = {}
        else:
            current_passport = {**current_passport, **{p.split(":")[0]: p.split(":")[1] for p in line.split(" ")}}

    passports.append(current_passport)
    return passports


if __name__ == '__main__':
    with open('day4.txt') as f:
        inp: list[str] = f.readlines()
        passports = split_to_passports(inp)

        valid_passport_count = 0
        valid_passport_count_part_two = 0
        for p in passports:
            if is_valid_passport(p):
                valid_passport_count += 1
            if is_valid_passport_part_two(p):
                valid_passport_count_part_two += 1

    print("There are %s valid passports in part 1" % valid_passport_count)
    print("There are %s valid passports in part 2" % valid_passport_count_part_two)
