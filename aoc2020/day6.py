# https://adventofcode.com/2020/day/6


def get_groups(lines: list[str]) -> list[list[str]]:
    groups = []
    current_group = []
    for line in lines:

        if not line.strip():
            groups.append(current_group)
            current_group = []
        else:
            current_group.append(line.strip())

    groups.append(current_group)

    return groups


def sum_group_answers(group_answers: list[str]) -> int:
    answered_questions = {}
    for person in group_answers:
        for answer in person:
            answered_questions[answer] = 0

    return len(answered_questions)


def sum_group_answers_part_two(group_answers: list[str]) -> int:
    answered_questions = {}
    for person in group_answers:
        for answer in person:
            if answer in answered_questions:
                answered_questions[answer] += 1
            else:
                answered_questions[answer] = 1

    return len([1 for v in answered_questions.values() if v == len(group_answers)])


if __name__ == '__main__':
    with open('day6.txt') as f:
        inp: list[str] = f.readlines()

        g_answers = get_groups(inp)
        answer_count = sum([sum_group_answers(g) for g in g_answers])
        print("The sum of answers for all groups are %s" % answer_count)

        answer_count = sum([sum_group_answers_part_two(g) for g in g_answers])
        print("The sum of answers for part two are %s" % answer_count)
