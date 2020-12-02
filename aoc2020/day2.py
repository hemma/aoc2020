# https://adventofcode.com/2020/day/2


def get_password_policy(line: str) -> tuple[int, int, str]:
    policy = line.split(':')[0]
    min_occ = policy.split('-')[0].strip()
    max_occ = policy.split('-')[1].strip().split(' ')[0].strip()
    letter = policy[-1]
    return int(min_occ), int(max_occ), letter


def get_password(line: str) -> str:
    return line.split(':')[1].strip()


def is_valid_password(password: str, policy: tuple[int, int, str]) -> bool:
    matches = password.count(policy[2])
    return policy[0] <= matches <= policy[1]


def is_valid_password_part_two(password: str, policy: tuple[int, int, str]) -> bool:
    return (password[policy[0] - 1] == policy[2] and not password[policy[1] - 1] == policy[2]) or (
                not password[policy[0] - 1] == policy[2] and password[policy[1] - 1] == policy[2])


if __name__ == '__main__':
    with open('day2.txt') as f:
        inp: list[str] = f.readlines()
        valid_password_count = 0
        valid_password_count_part_two = 0
        for p in inp:
            if is_valid_password(get_password(p), get_password_policy(p)):
                valid_password_count += 1
            if is_valid_password_part_two(get_password(p), get_password_policy(p)):
                valid_password_count_part_two += 1

        print("There are %s valid passwords." % valid_password_count)
        print("There are %s valid passwords for part two." % valid_password_count_part_two)
