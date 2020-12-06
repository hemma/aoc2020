# https://adventofcode.com/2020/day/5
import math


def get_seat_id(row: int, colum: int) -> int:
    return row * 8 + colum


def get_seat(line: str) -> tuple[int, int]:
    row = (0, 127)
    column = (0, 7)
    for c in line:
        if c in ['B', 'F']:
            row = bsp(c, row)
        if c in ['R', 'L']:
            column = bsp(c, column, 'R', 'L')

    return row[0], column[0]


def bsp(c: str, r: tuple[int, int], u_c: str = 'B', l_c='F') -> tuple[int, int]:
    if c == u_c:
        return r[0] + math.ceil((r[1] - r[0]) / 2), r[1]
    if c == l_c:
        return r[0], r[0] + math.floor((r[1] - r[0]) / 2)


def find_my_seat(seat_ids: list[int]) -> int:
    last_seat_id = -1000
    for s_id in seat_ids:
        if s_id == last_seat_id + 2:
            return last_seat_id + 1
        last_seat_id = s_id
    return -1


if __name__ == '__main__':
    with open('day5.txt') as f:
        inp: list[str] = f.readlines()

        highest_seat_id = -1
        all_seat_ids = []
        for bp in inp:
            seat_id = get_seat_id(*get_seat(bp))
            if seat_id > highest_seat_id:
                highest_seat_id = seat_id
            all_seat_ids.append(seat_id)

        all_seat_ids = sorted(all_seat_ids)

        my_seat_id = find_my_seat(all_seat_ids)

        print("Highest seat id %s" % highest_seat_id)
        print("My seat id is %s" % my_seat_id)
