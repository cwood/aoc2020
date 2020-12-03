#!/usr/bin/env python3

from collections import Counter, namedtuple

tree = "#"

Pos = namedtuple("Pos", ["down", "right"])


class Slope:

    def __init__(self, slope):
        self.slope = slope
        self.slope_len = len(self.slope) - 1

    def to_position(self, x):
        def to_string(item):
            return "tree" if item == tree else "free"

        if x <= self.slope_len:
            return to_string(self.slope[x])

        start = 0

        while x > self.slope_len:
            slope = self.slope * start  # brute force :-/
            if len(slope)-1 < x:
                start += 1
                continue
            return to_string(slope[x])


def traverse(pos, nextpos, slopes, counter):
    obj = slopes[pos.down-1].to_position(pos.right-1)
    counter[obj] += 1

    try:
        return traverse(Pos(pos.down+nextpos.down, pos.right+nextpos.right), nextpos, slopes, counter)
    except IndexError:
        return


if __name__ == "__main__":
    testslopes = [Slope(s) for s in open("testinput").read().split("\n") if s]
    test_slopes_found = Counter(tree=0, free=0)
    traverse(Pos(1, 1), Pos(down=1, right=3), testslopes, test_slopes_found)

    assert test_slopes_found["tree"] == 7
    print("Found 7 trees from the test slope")


    """
    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.
    """

    test_found_trees = None

    for nextpos in [Pos(1, 1), Pos(1, 3), Pos(1, 5), Pos(1, 7), Pos(2, 1)]:
        found = Counter(tree=0, free=0)
        traverse(Pos(1, 1), nextpos, testslopes, found)
        test_found_trees = (found["tree"] * test_found_trees) if test_found_trees is not None else found["tree"]

    assert test_found_trees == 336
    print("Found 336 trees from the test slope routes")

    slopes = [Slope(s) for s in open("input").read().split("\n") if s]
    slopes_found = Counter(tree=0, free=0)
    traverse(Pos(1, 1), Pos(down=1, right=3), slopes, slopes_found)
    print("Part 1: Trees %s Free %s" % (slopes_found["tree"], slopes_found["free"]))

    """
    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.
    """

    found_trees = None

    for nextpos in [Pos(1, 1), Pos(1, 3), Pos(1, 5), Pos(1, 7), Pos(2, 1)]:
        found = Counter(tree=0, free=0)
        traverse(Pos(1, 1), nextpos, slopes, found)
        found_trees = found["tree"] * found_trees if found_trees is not None else found["tree"]

    print("Part 2: %s" % found_trees)
