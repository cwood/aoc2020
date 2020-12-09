#!/usr/bin/env python3


def parse_raw_rules(rules):
    def parse_bag(bag):
        bag = bag.strip()
        try:
            num = int(bag[0])
            bag_color = " ".join(bag.split(" ")[1:3])
        except ValueError:
            num = None
            bag_color = " ".join(bag.split(" ")[:2])

        return num, bag_color

    bag_rules = {}

    for rule in rules:
        root_bag, child_bags = rule.split("contain", 1)

        root, root_color = parse_bag(root_bag)
        bag_rules[root_color] = {}

        if "no other bags." in child_bags:
            continue

        for child_bag in child_bags.split(","):
            num, color = parse_bag(child_bag)
            bag_rules[root_color].update({color: num})

    return bag_rules


def found_root_bags(rules, bag_color, found=None):
    if found is None:
        found = set()

    for outer_bag, inner_bags in rules.items():
        if bag_color in inner_bags:
            found.add(outer_bag)
            found_root_bags(rules, outer_bag, found=found)

    return found


def outer_bag_combo(rules, bag_color):
    inner_bags = rules[bag_color]

    if inner_bags is None:
        return 0

    total_bags = sum(inner_bags.values())

    for inner_bag, count in inner_bags.items():
        total_bags = total_bags + count*outer_bag_combo(rules, inner_bag)

    return total_bags


if __name__ == "__main__":

    testrules = parse_raw_rules(open('testinput').readlines())

    found = found_root_bags(testrules, "shiny gold")
    total_bags = outer_bag_combo(testrules, "shiny gold")
    assert len(found) == 4
    assert total_bags == 32
    print("Success!")

    rules = parse_raw_rules(open('input').readlines())
    found = found_root_bags(rules, "shiny gold")
    print("Part 1: %s" % (len(found)))
    print("Part 2: %s" % (outer_bag_combo(rules, "shiny gold")))
