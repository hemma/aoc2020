# https://adventofcode.com/2020/day/3


def count_encountered_trees(toboggan_map: list[list[str]], movement: dict) -> int:
    current_x = 0
    current_y = 0
    tree_count = 0
    current_x += movement['x']
    current_y += movement['y']
    while current_y < len(toboggan_map):
        if toboggan_map[current_y][current_x] == "#":
            tree_count += 1
            
        current_x += movement['x']
        current_x %= len(toboggan_map[current_y])
        current_y += movement['y']

    return tree_count


def lines_to_map(lines: list[str]) -> list[list[str]]:
    return [list(line.strip()) for line in lines]


if __name__ == '__main__':
    with open('day3.txt') as f:
        inp: list[str] = f.readlines()
        movement_part_1 = {'x': 3, 'y': 1}
        trees = count_encountered_trees(lines_to_map(inp), movement_part_1)

        print("There are %s trees" % trees)

        trees_multiplied = 1
        for movement_part_2 in [{'y': 1, 'x': 3}, {'y': 1, 'x': 1}, {'y': 1, 'x': 5}, {'y': 1, 'x': 7},
                                {'y': 2, 'x': 1}]:
            trees_multiplied *= count_encountered_trees(lines_to_map(inp), movement_part_2)
        print("Part two %s" % trees_multiplied)
