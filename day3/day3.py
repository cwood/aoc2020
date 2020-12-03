#!/usr/bin/env python3

from collections import Counter

tree = "#"

class Slope:

    def __init__(self, slope):
        self.slope = slope
        self.slope_len = len(self.slope)

    def to_position(self, x):
        def to_string(item):
            return "tree" if item is tree else "free"

        if x <= self.slope_len:
            return to_string(self.slope[x])

        start = 1

        while x > self.slope_len:
            new_len = self.slope_len * start
            if new_len < x:
                start+=1
                continue

            x =  new_len - x

        return to_string(self.slope[x])

def traverse(down, right, slopes, counter):
    pos = slopes[down].to_position(right)
    counter[pos] +=1
    print(counter)

    try:
        return traverse(down+1, right+3, slopes, counter)
    except IndexError:
        return


if __name__ == "__main__":
    slopes = [Slope(s) for s in open("input").read().split("\n") if s]

    slopes_found = Counter(tree=0, free=0)
    traverse(1, 3, slopes, slopes_found)
    print("Trees %s Free %s" % (slopes_found["tree"], slopes_found["free"]))
