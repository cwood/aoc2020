#!/usr/bin/env python3

def missing_sum_window(numbers, preamble_size=25):

    def is_in_sum(window, num):
        i = 0
        while i <= len(window)-1:
            j = 0
            while j <= len(window)-1:
                f, s = window[i], window[j]
                total = sum([f, s])
                if total == num:
                    return True
                j += 1
            i += 1
        return False

    i = preamble_size
    while i <= len(numbers):
        preamble = numbers[i-preamble_size:i]
        if not is_in_sum(preamble, numbers[i]):
            return numbers[i]
        i += 1


def find_weakness_sum(numbers, missing_sum):
    def smallest_largest_sum(window):
        smallest, largest = window[0], window[0]
        for i in window:
            if i < smallest:
                smallest = i

            if i > largest:
                largest = i

        return sum([smallest, largest])

    window_size = 2
    while True:
        i = 0
        while i <= len(numbers)-1:
            window = numbers[i:i+window_size]
            total = sum(numbers[i:i+window_size])
            if total == missing_sum:
                return smallest_largest_sum(window)
            i += 1
        window_size += 1


if __name__ == "__main__":
    testnumbers = [int(i) for i in open('testinput').readlines() if i]
    missing_sum = missing_sum_window(testnumbers, preamble_size=5)
    assert missing_sum == 127
    print("Success Part One!")

    weakness_number = find_weakness_sum(testnumbers, missing_sum)
    assert weakness_number == 62
    print("Success Part Two!")

    numbers = [int(i) for i in open('input').readlines() if i]
    missing_sum = missing_sum_window(numbers)
    print("Part 1: %s" % (missing_sum))

    weakness_number = find_weakness_sum(numbers, missing_sum)
    print("Part 2: %s" % (weakness_number))
