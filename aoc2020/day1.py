# https://adventofcode.com/2020/day/1

def find_two_entry_sum_2020(entries: list[int]) -> tuple[int, int]:
    for x in entries:
        for y in entries:
            if x + y == 2020:
                return x, y
    raise Exception("No entries that sum to 2020 found.")


def find_three_entry_sum_2020(entries: list[int]) -> tuple[int, int, int]:
    for x in entries:
        for y in entries:
            for z in entries:
                if x + y + z == 2020:
                    return x, y, z
    raise Exception("No entries that sum to 2020 found.")


if __name__ == '__main__':
    with open('day1_1.txt') as f:
        inp: list[str] = f.readlines()
        inp_int = [int(x) for x in inp]

        x, y = find_two_entry_sum_2020(inp_int)
        print("Answer for part one is %s" % (x * y))

        x, y, z = find_three_entry_sum_2020(inp_int)
        print("Answer for part two is %s" % (x * y * z))
