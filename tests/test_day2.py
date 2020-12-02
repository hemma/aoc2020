from aoc2020.day2 import get_password_policy, get_password, is_valid_password, is_valid_password_part_two

INP = ["1 - 3 a: abcde",
       "1 - 3 b: cdefg",
       "2 - 9 c: ccccccccc", ]


def test_get_password_policy():
    policy = get_password_policy(INP[0])
    assert policy == (1, 3, 'a')

    policy = get_password_policy(INP[1])
    assert policy == (1, 3, 'b')

    policy = get_password_policy(INP[2])
    assert policy == (2, 9, 'c')


def test_get_password():
    password = get_password(INP[0])
    assert password == "abcde"
    password = get_password(INP[1])
    assert password == "cdefg"
    password = get_password(INP[2])
    assert password == "ccccccccc"


def test_is_valid_password():
    assert is_valid_password(get_password(INP[0]), get_password_policy(INP[0]))
    assert not is_valid_password(get_password(INP[1]), get_password_policy(INP[1]))
    assert is_valid_password(get_password(INP[2]), get_password_policy(INP[2]))


def test_is_valid_password_part_two():
    assert is_valid_password_part_two(get_password(INP[0]), get_password_policy(INP[0]))
    assert not is_valid_password_part_two(get_password(INP[1]), get_password_policy(INP[1]))
    assert not is_valid_password_part_two(get_password(INP[2]), get_password_policy(INP[2]))
