#!/usr/bin/env python3

from collections import Counter

def all_customs(raw_customs):

    answered = []

    for group in raw_customs:
        persons = [l for l in group.split("\n") if l]
        group_counter = Counter()
        for person in persons:
            group_counter = Counter(person) + group_counter

        most_common = group_counter.most_common()
        for letter, value in group_counter.items():
            if value == len(persons):
                answered.append(1)

    return sum(answered)


def sum_customs(raw_customs):

    answered = []

    for custom in raw_customs:
        answers = set(custom.replace("\n", ""))
        answered.append(len(answers))

    return sum(answered)


if __name__ == "__main__":

    testcustoms = [l for l in open("testinput").read().split("\n\n") if l]

    assert sum_customs(testcustoms) == 11
    assert all_customs(testcustoms) == 6
    print("Success!")

    customs = [l for l in open("input").read().split("\n\n") if l]
    print("Customs Sum: %s" % (sum_customs(customs)))
    print("All Sum: %s" % (all_customs(customs)))
