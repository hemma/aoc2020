from aoc2020.day6 import get_groups, sum_group_answers, sum_group_answers_part_two

INP = [
    "abc",
    "",
    "a",
    "b",
    "c",
    "",
    "ab",
    "ac",
    "",
    "a",
    "a",
    "a",
    "a",
    "",
    "b"
]


def test_get_groups():
    groups = get_groups(INP)
    assert len(groups) == 5
    assert groups[0] == ["abc"]
    assert groups[1] == ["a", "b", "c"]


def test_sum_group_answers():
    assert sum_group_answers(get_groups(INP)[0]) == 3
    assert sum_group_answers(get_groups(INP)[1]) == 3
    assert sum_group_answers(get_groups(INP)[2]) == 3
    assert sum_group_answers(get_groups(INP)[3]) == 1


def test_sum_group_answers_part_two():
    assert sum_group_answers_part_two(get_groups(INP)[0]) == 3
    assert sum_group_answers_part_two(get_groups(INP)[1]) == 0
    assert sum_group_answers_part_two(get_groups(INP)[2]) == 1