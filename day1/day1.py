#!/usr/bin/env python3

def threeSum(numbers, sumTo):
    for n in numbers:
        for i in numbers:
            for c in numbers:
                if n + i + c == sumTo:
                    return n * i * c

if __name__ == "__main__":
    numbers = [int(n) for n in open("input").read().split("\n") if n]
    answer = next(n * (abs(n - 2020)) for n in numbers if abs(n - 2020) in numbers)

    print("Part 1: %s" % answer)
    print("Part 2: %s" % (threeSum(numbers, 2020)))
