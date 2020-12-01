from aoc2020 import __version__
from aoc2020.day1 import find_two_entry_sum_2020, find_three_entry_sum_2020


def test_find_two_entry_sum_2020():
    entries = [1721, 979, 366, 299, 675, 1456]
    x, y = find_two_entry_sum_2020(entries)

    assert x == 1721
    assert y == 299


def test_find_three_entry_sum_2020():
    entries = [1721, 979, 366, 299, 675, 1456]
    x, y, z = find_three_entry_sum_2020(entries)

    assert x == 979
    assert y == 366
    assert z == 675
