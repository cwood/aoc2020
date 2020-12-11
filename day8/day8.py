#!/usr/bin/env python3


def parse_program(raw_program):
    program = []

    for line in raw_program:
        op, num = line.split(" ")
        pos, num = num[0], int(num[1:len(num)-1])
        if pos == "-":
            num = -num
        program.append([op, num])

    return program


def acc_repeat_stopper(program):

    acc = 0
    i = 0

    lines_executed = set()

    while i <= len(program)-1:
        if i in lines_executed:
            break

        lines_executed.add(i)

        op, num = program[i][0], program[i][1]

        if op == "acc":
            acc = acc + num
            i += 1
        elif op == "nop":
            i += 1
        elif op == "jmp":
            i += num

    return acc


def acc_completed_stopper(program, replaced=None):
    acc, i, line_replaced = 0, 0, None

    if replaced is None:
        replaced = set()

    lines_executed = set()

    original = program.copy()

    while i <= len(program)-1:
        if i in lines_executed and line_replaced == i:
            return acc_completed_stopper(original, replaced=replaced)

        op, num = program[i][0], program[i][1]

        lines_executed.add(i)

        if op == "acc":
            acc = acc + num
            i += 1
            continue

        if i not in replaced and line_replaced is not None:
            replaced.add(i)
            line_replaced = i

            if op == "nop":
                op = "jmp"
            elif op == "jmp":
                op = "nop"

        if op == "nop":
            i += 1
        elif op == "jmp":
            i += num

    print(acc)
    return acc


if __name__ == "__main__":
    testprogram = open("testinput").readlines()
    testprogram = parse_program(testprogram)
    assert acc_repeat_stopper(testprogram) == 5
    assert acc_completed_stopper(testprogram) == 8

    raw_program = open("input").readlines()
    program = parse_program(raw_program)
    print("Part 1: %s" % acc_repeat_stopper(program))
    print("Part 2: %s" % acc_completed_stopper(program))
