#!/usr/bin/env python3

seat_id_multiplier = 8

# FBFBBFFRLR
def seat_id_from_string(seat_id_pattern):
    def parse_pattern(row_identifier, upper_char, lower_char, startrange):
        rows = list(startrange)
        row_id = 0
        for p in row_identifier:
            half = int(len(rows)/2)

            if  upper_char == p:
                rows = rows[:half]
            elif lower_char == p:
                rows = rows[-half:]

            if len(rows) == 1:
                row_id = rows[0]
        return row_id

    row_identifier = seat_id_pattern[:7]
    column_identifier = seat_id_pattern[-3:]

    row_id = parse_pattern(row_identifier, "F", "B", range(128))
    column_id = parse_pattern(column_identifier, "L", "R", range(8))

    return (row_id * seat_id_multiplier) + column_id

if __name__ == "__main__":

    for seat_value, seat_string in {
        567: "BFFFBBFRRR",
        119: "FFFBBBFRRR",
        820: "BBFFBBFRLL"
    }.items():
        seat_id = seat_id_from_string(seat_string)
        assert seat_id == seat_value

    plane_tickets = [l for l in open("input").read().split("\n") if l]

    highest, seat_ids = 0, []

    for ticket in plane_tickets:
        seat_id = seat_id_from_string(ticket)
        if seat_id > highest:
            highest = seat_id
        seat_ids.append(seat_id)

    print("Highest: %s" % (highest))
    seat_ids.sort()

    complete = set(range(seat_ids[0], seat_ids[len(seat_ids)-1]))
    diff = complete - set(seat_ids)

    print("Missing seats: %s" % (diff))
