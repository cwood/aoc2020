#!/usr/bin/env python3

from collections import Counter


def jolt_differences(jolts):

    jolts.sort()

    diffs = Counter()

    i = 0
    while i <= len(jolts)-1:
        cjolt = jolts[i]
        if i == 0:
            diffs[cjolt] += 1

        try:
            d = jolts[i+1] - cjolt
        except IndexError:
            d = jolts[i]+3 - cjolt

        diffs[d] += 1
        i += 1

    return diffs


def jolt_possibilities(jolts):

    jolts.sort()

    total_arrangements = {0: 1}
    i = 0
    while i <= len(jolts)-1:
        cjolt = jolts[i]
        options = [cjolt-1, cjolt-2, cjolt-3]
        n = 0
        for o in options:
            n += total_arrangements.get(o, 0)
        total_arrangements[cjolt] = n
        i += 1

    return total_arrangements[jolts[-1]]


if __name__ == "__main__":
    assert jolt_possibilities([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]) == 8

    testjolts = [int(i) for i in open("testinput").readlines() if i]
    diff = jolt_differences(testjolts)
    assert diff[1] * diff[3] == 22 * 10  # 22 one jolts and 10 3 jolts
    possible = jolt_possibilities(testjolts)
    assert possible == 19208

    jolts = [int(i) for i in open("input").readlines() if i]
    realdiff = jolt_differences(jolts)
    print("Part 1: %s" % (realdiff[1] * realdiff[3]))
    print("Part 2: %s" % (jolt_possibilities(jolts)))
