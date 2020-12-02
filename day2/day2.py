#!/usr/bin/env python3

from collections import Counter

class Password:

    def __init__(self, minmax, char, password):
        self.minmax = [int(i) for i in minmax.split("-")]
        self.char = char
        self.password = self.password_to_python(password)

    def password_to_python(self, password):
        return Counter(password)

    def is_valid(self):
        if self.password[self.char] == 0:
            return False

        minn = self.minmax[0]
        maxx = self.minmax[1]

        count = self.password[self.char]

        if count < minn:
            return False

        if count > maxx:
            return False

        return True


class PasswordPos(Password):

    def password_to_python(self, password):
        return password

    def is_valid(self):
        if self.char not in self.password:
            return False

        pos1, pos2 = self.minmax

        matches = (self.password[pos1-1] == self.char,
                   self.password[pos2-1] == self.char)

        if (not any(matches) or all(matches)):
            return False

        return True



if __name__ == "__main__":

    lines = [l for l in open("input").read().split("\n") if l]
    part1valid = 0
    part2valid = 0

    for line in lines:
        try:
            minmax, charcolon, password = line.split(" ", 3)
            if Password(minmax, charcolon[0], password).is_valid():
                part1valid+=1
            if PasswordPos(minmax, charcolon[0], password).is_valid():
                part2valid+=1
        except ValueError:
            print(line)

    print("Part 1:%s" % (part1valid))
    print("Part 2:%s" % (part2valid))
