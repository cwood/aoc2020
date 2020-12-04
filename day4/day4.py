#!/usr/bin/env python3

import re


class Rule:
    def __init__(self, value):
        self.value = value

    def is_valid(self):
        raise NotImplementedError


class IntRule(Rule):
    at_least = None
    at_most = None

    def __str__(self):
        return "IntRule(%s <= %s <= %s)" % (self.at_least, self.value, self.at_most)

    def is_valid(self):
        byr = int(self.value)
        return self.at_least <= byr <= self.at_most


class Byr(IntRule):
    at_least = 1920
    at_most = 2002


class Iyr(IntRule):
    at_least = 2010
    at_most = 2020


class Eyr(IntRule):
    at_least = 2020
    at_most = 2030


class In(IntRule):
    at_least = 59
    at_most = 76


class Cm(IntRule):
    at_least = 150
    at_most = 193


class Hgt(Rule):

    def __str__(self):
        return "Hgt(%s)" % (self.value)

    def is_valid(self):
        suffix = ["cm", "in"]
        if not any([f for f in suffix if f in self.value]):
            return False

        if self.value.endswith("in"):
            return In(self.value[:-2]).is_valid()

        return Cm(self.value[:-2]).is_valid()


class Hcl(Rule):
    hexpattern = re.compile(r'^#[0-9a-f]{6}$')

    def __str__(self):
        return "Hcl(%s %s)" % (self.value, self.hexpattern.search(self.value))

    def is_valid(self):
        return True if self.hexpattern.match(self.value) else False


class Ecl(Rule):

    colors = [
        "amb", "blu", "brn", "gry", "grn", "hzl", "oth"
    ]

    def __str__(self):
        return "Ecl(%s %s)" % (self.value, self.value in self.colors)


    def is_valid(self):
        return self.value in self.colors


class Pid(Rule):

    pidnumber = re.compile(r'^[0-9]{9}$')

    def __str__(self):
        return "Pid(%s %s)" % (self.value, self.pidnumber.match(self.value))

    def is_valid(self):
        return True if self.pidnumber.match(self.value) else False


required_rules = {
    "byr": Byr,  # (Birth Year) - four digits; at least 1920 and at most 2002.
    "iyr": Iyr,  # (Issue Year) - four digits; at least 2010 and at most 2020.
    "eyr": Eyr,  # (Expiration Year) - four digits; at least 2020 and at most 2030.
    "hgt": Hgt,  # (Height) - a number followed by either cm or in:
                 # If cm, the number must be at least 150 and at most 193.
                 # If in, the number must be at least 59 and at most 76.

    "hcl": Hcl,  # (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    "ecl": Ecl,  # (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    "pid": Pid,  # (Passport ID) - a nine-digit number, including leading zeroes.
}

required_fields = set(required_rules.keys())

optional = {
    "cid"  # (Country ID) - ignored, missing or not.
}


def parse_passports(passports):
    for rawpassport in passports:
        lines = rawpassport.split("\n")
        linefields = [l.split(" ") for l in lines]
        passport = {}
        for l in linefields:
            for f in l:
                key, sep, value = f.partition(":")
                passport[key] = value
        yield passport


def validate_raw_passports(passports):

    validfields = 0
    validpassports = 0

    for passport in parse_passports(passports):
        if required_fields.issubset(passport.keys()):
            validfields += 1

            fields_validated = []
            for field, value in passport.items():
                try:
                    fields_validated.append(
                        required_rules[field](value).is_valid()
                    )
                except KeyError:
                    continue

            if all(fields_validated):
                validpassports += 1

    return validfields, validpassports


if __name__ == "__main__":
    testpassports = [l for l in open("testinput").read().split("\n\n") if l]
    validfields, validpassports = validate_raw_passports(testpassports)
    assert validfields == 2

    testvalidpassports = [l for l in open("validpassports").read().split("\n\n") if l]
    validfields, validpassports = validate_raw_passports(testvalidpassports)

    testinvalidpassports = [l for l in open("invalidpassports").read().split("\n\n") if l]
    invalidfields, invalidpassports = validate_raw_passports(testinvalidpassports)

    assert invalidpassports == 0
    assert validpassports == 4

    passports = [l for l in open("input").read().split("\n\n") if l]
    validfields, validpassports = validate_raw_passports(passports)

    print("Part 1: %s" % (validfields))
    print("Part 2: %s" % (validpassports))
