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

    jolts.append(0)
    jolts.sort()
    jolts.insert(len(jolts), jolts[len(jolts)-1]+3)

    pos = 1
    i = 0
    while i <= len(jolts)-1:
        cjolt = jolts[i]

        total_opts = 0
        j = 0
        while j <= len(jolts[0:i])-1:
            jjolt = jolts[j]
            for a in [1, 2, 3]:
                if jjolt + a == cjolt:
                    total_opts += 1
            j += 1
        i += 1

        print(pos, total_opts)

    print(pos)
    return pos


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
