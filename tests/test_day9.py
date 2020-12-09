from aoc2020.day9 import find_sum_of_last_x, find_start_end_contiguous_set_sum

INP = [
    35,
    20,
    15,
    25,
    47,
    40,
    62,
    55,
    65,
    95,
    102,
    117,
    150,
    182,
    127,
    219,
    299,
    277,
    309,
    576,
]


def test_find_sum_of_last_x():
    assert find_sum_of_last_x(INP, 5) == 127


def test_find_start_end_contiguous_set_sum():
    assert find_start_end_contiguous_set_sum(INP[0:INP.index(127)], 127) == (15, 47)
