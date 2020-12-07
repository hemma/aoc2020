from aoc2020.day7 import get_color_rules, count_bag_colors_can_contain

INP = [
    "light red bags contain 1 bright white bag, 2 muted yellow bags.",
    "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
    "bright white bags contain 1 shiny gold bag.",
    "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
    "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
    "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
    "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
    "faded blue bags contain no other bags.",
    "dotted black bags contain no other bags.",
]


def test_get_color_rules():
    colors = get_color_rules(INP)
    assert colors == {
        "light red": ["bright white", "muted yellow"],
        "dark orange": ["bright white", "muted yellow"],
        "bright white": ["shiny gold"],
        "muted yellow": ["shiny gold", "faded blue"],
        "shiny gold": ["dark olive", "vibrant plum"],
        "dark olive": ["faded blue", "dotted black"],
        "vibrant plum": ["faded blue", "dotted black"],
        "faded blue": [],
        "dotted black": []
    }


def test_count_bag_colors_can_contain():
    color_rules = get_color_rules(INP)
    assert count_bag_colors_can_contain(color_rules, "shiny gold") == 4
