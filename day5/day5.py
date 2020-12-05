#!/usr/bin/env python3

seat_id_multiplier = 8

# FBFBBFFRLR
def seat_id_from_string(seat_id_pattern):
    row_identifier = seat_id_pattern[:7]
    column_identifier = seat_id_pattern[-3:]

    row_id = 0
    rows = list(range(128))
    for p in row_identifier:

        half = int(len(rows)/2)

        if "F" == p:
            rows = rows[:half]
        elif "B" == p:
            rows = rows[-half:]

        if len(rows) == 1:
            row_id = rows[0]

    plane_column = 0
    plane_columns = list(range(8))
    for r in column_identifier:
        half = int(len(plane_columns)/2)
        if r == "R":
            plane_columns = plane_columns[-half:]
        elif r == "L":
            plane_columns = plane_columns[:half]

        if len(plane_columns) == 1:
            plane_column = plane_columns[0]

    return (row_id * seat_id_multiplier) + plane_column

if __name__ == "__main__":

    for seat_value, seat_string in {
        567: "BFFFBBFRRR",
        119: "FFFBBBFRRR",
        820: "BBFFBBFRLL"
    }.items():
        seat_id = seat_id_from_string(seat_string)
        assert seat_id == seat_value

    plane_tickets = [l for l in open("input").read().split("\n") if l]

    highest = 0
    seat_ids = []

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
