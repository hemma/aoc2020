# https://adventofcode.com/2020/day/9


def find_sum_of_last_x(numbers: list[int], last: int) -> int:
    for i, s in enumerate(numbers[last:]):
        index = i + last
        match = False
        for x in numbers[index - last:index]:
            if match:
                continue
            for y in numbers[index - last + 1:index]:
                if match:
                    continue
                if x + y == s:
                    match = True

        if not match:
            return s

    return numbers[-1]


def find_start_end_contiguous_set_sum(numbers: list[int], x: int) -> tuple[int, int]:
    for start in range(0, len(numbers) - 1):
        for end in range(1, len(numbers)):
            if sum(numbers[start:end]) > x:
                break
            if sum(numbers[start:end]) == x:
                r = numbers[start:end]
                return min(r), max(r)

    return -1, -1


if __name__ == '__main__':
    with open('day9.txt') as f:
        inp: list[str] = f.readlines()
        inp_int = [int(x.strip()) for x in inp]

        last_match = find_sum_of_last_x(inp_int, 25)

        print("Last match: %s" % last_match)

        s, e = find_start_end_contiguous_set_sum(inp_int, last_match)

        print("Part two: %s" % (s + e))
