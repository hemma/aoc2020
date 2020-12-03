from aoc2020.day3 import count_encountered_trees, lines_to_map

INP = [
    "..##.......",
    "#...#...#..",
    ".#....#..#.",
    "..#.#...#.#",
    ".#...##..#.",
    "..#.##.....",
    ".#.#.#....#",
    ".#........#",
    "#.##...#...",
    "#...##....#",
    ".#..#...#.#"
]


def test_lines_to_map():
    small_map = [
        ".#..",
        "##.."
    ]
    expected_map = [
        [".", "#", ".", "."],
        ["#", "#", ".", "."]
    ]

    assert lines_to_map(small_map) == expected_map


def test_count_encountered_trees():
    assert count_encountered_trees(lines_to_map(INP), {'y': 1, 'x': 3}) == 7
    assert count_encountered_trees(lines_to_map(INP), {'y': 1, 'x': 1}) == 2
    assert count_encountered_trees(lines_to_map(INP), {'y': 1, 'x': 5}) == 3
    assert count_encountered_trees(lines_to_map(INP), {'y': 1, 'x': 7}) == 4
    assert count_encountered_trees(lines_to_map(INP), {'y': 2, 'x': 1}) == 2

