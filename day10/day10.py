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


if __name__ == "__main__":
    testjolts = [int(i) for i in open("testinput").readlines() if i]
    diff = jolt_differences(testjolts)
    assert diff[1] * diff[3] == 22 * 10  # 22 one jolts and 10 3 jolts

    jolts = [int(i) for i in open("input").readlines() if i]
    realdiff = jolt_differences(jolts)
    print("Part 1: %s" % (realdiff[1] * realdiff[3]))
