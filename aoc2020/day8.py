# https://adventofcode.com/2020/day/8

def get_operation(line: str) -> tuple[str, int]:
    op, val = line.split(" ")
    val = int(val[1:]) if val.startswith("+") else -int(val[1:])
    return op, val


def run_until_infinite_loop_detected(program: list[str]) -> int:
    acc = 0
    index = 0
    visited_instructions = set()
    while index not in visited_instructions:
        visited_instructions.add(index)
        operation = get_operation(program[index])
        if operation[0] == "acc":
            acc += operation[1]
            index += 1
        elif operation[0] == "jmp":
            index += operation[1]
        else:
            index += 1

    return acc


def run_and_fix_infinite_loop(program: list[str]) -> int:
    changed_instruction = set()
    while True:
        edited_program = program.copy()
        has_changed_instruction = False
        acc = 0
        index = 0
        visited_instructions = set()
        while index not in visited_instructions:
            if index == len(program):
                return acc
            visited_instructions.add(index)
            operation = get_operation(edited_program[index])
            if operation[0] == "acc":
                acc += operation[1]
                index += 1
            elif operation[0] == "jmp":
                if not has_changed_instruction and index not in changed_instruction:
                    has_changed_instruction = True
                    changed_instruction.add(index)
                    edited_program[index] = "{} {}".format("nop", "+" + str(operation[1]) if operation[1] >= 0 else str(
                        operation[1]))
                    visited_instructions.remove(index)
                else:
                    index += operation[1]
            else:
                if not has_changed_instruction and index not in changed_instruction:
                    has_changed_instruction = True
                    changed_instruction.add(index)
                    edited_program[index] = "{} {}".format("jmp", "+" + str(operation[1]) if operation[1] >= 0 else str(
                        operation[1]))
                    visited_instructions.remove(index)
                else:
                    index += 1


if __name__ == '__main__':
    with open('day8.txt') as f:
        inp: list[str] = f.readlines()

        acc_val = run_until_infinite_loop_detected(inp)

        print("Accumulator value before termination is %s" % acc_val)

        acc_val_fixed = run_and_fix_infinite_loop(inp)

        print("Accumulator value after fix is %s" % acc_val_fixed)
