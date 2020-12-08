from aoc2020.day8 import run_until_infinite_loop_detected, get_operation, run_and_fix_infinite_loop

INP = [
    "nop +0",
    "acc +1",
    "jmp +4",
    "acc +3",
    "jmp -3",
    "acc -99",
    "acc +1",
    "jmp -4",
    "acc +6",
]


def test_get_operation():
    assert get_operation(INP[0]) == ("nop", 0)
    assert get_operation(INP[1]) == ("acc", 1)
    assert get_operation(INP[2]) == ("jmp", 4)
    assert get_operation(INP[4]) == ("jmp", -3)


def test_run_until_infinite_loop_detected():
    assert run_until_infinite_loop_detected(INP) == 5


def test_run_and_fix_infinite_loop():
    assert run_and_fix_infinite_loop(INP) == 8
