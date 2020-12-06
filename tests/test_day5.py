from aoc2020.day5 import get_seat, bsp, get_seat_id, find_my_seat

INP = [
    "BFFFBBFRRR",
    "FFFBBBFRRR",
    "BBFFBBFRLL",

]


#: row 70, column 7, seat ID 567.
#: row 14, column 7, seat ID 119.
#: row 102, column 4, seat ID 820.

def test_get_seat():
    assert get_seat(INP[0]) == (70, 7)
    assert get_seat(INP[1]) == (14, 7)
    assert get_seat(INP[2]) == (102, 4)


def test_get_seat_id():
    assert get_seat_id(*get_seat(INP[0])) == 567
    assert get_seat_id(*get_seat(INP[1])) == 119
    assert get_seat_id(*get_seat(INP[2])) == 820


def test_bsp():
    assert bsp('B', (0, 127)) == (64, 127)

    assert bsp('F', (0, 127)) == (0, 63)
    assert bsp('B', (0, 63)) == (32, 63)
    assert bsp('F', (32, 63)) == (32, 47)
    assert bsp('B', (32, 47)) == (40, 47)
    assert bsp('B', (40, 47)) == (44, 47)
    assert bsp('F', (44, 47)) == (44, 45)
    assert bsp('F', (44, 45)) == (44, 44)
    assert bsp('B', (44, 45)) == (45, 45)


def test_find_my_seat():
    assert find_my_seat([40, 41, 42, 43, 44, 45, 46, 47, 49, 50, 51, 52, 53, 54, 55]) == 48
