#!/usr/bin/env python3


def parse_program(raw_program):
    program = []

    for line in raw_program:
        op, num = line.split(" ")
        pos, num = num[0], int(num[1:len(num)-1])
        if pos == "-":
            num = -num
        program.append((op, num))

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


if __name__ == "__main__":
    testprogram = open("testinput").readlines()
    testprogram = parse_program(testprogram)
    assert acc_repeat_stopper(testprogram) == 5

    raw_program = open("input").readlines()
    program = parse_program(raw_program)
    print("Part 1: %s" % acc_repeat_stopper(program))
