# https://adventofcode.com/2020/day/7
import re


def get_color_rules(lines: list[str]) -> dict[str, list]:
    color_rules = {}
    for line in lines:
        outer_color = line.split("bags")[0].strip()
        inner_colors = re.findall("\\d ([a-z ]* )", line.split("contain")[1])
        color_rules[outer_color] = [x.strip() for x in inner_colors]

    return color_rules


def count_bag_colors_can_contain(color_rules: dict[str, list], color: str) -> int:
    count = 0
    for key in color_rules.keys():
        if can_contain_color(color_rules, key, color):
            count += 1

    return count


def can_contain_color(color_rules: dict[str, list], color_key: str, color_to_match: str) -> bool:
    for color in color_rules[color_key]:
        a = color_rules[color_key]
        if color == color_to_match:
            return True
        else:
            if can_contain_color(color_rules, color, color_to_match):
                return True
    return False


if __name__ == '__main__':
    with open('day7.txt') as f:
        inp: list[str] = f.readlines()
        rules = get_color_rules(inp)
        bag_count = count_bag_colors_can_contain(rules, "shiny gold")

        print("Part one %s" % bag_count)
