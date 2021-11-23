#!/usr/bin/env python3

OCCUPIED = "#"
FLOOR = "."
SEAT = "L"

POSITIONS = [
    (-1, 0),  # Up
    (1, 0),  # Down
    (0, -1),  # Left
    (0, 1),  # Right
    (-1, -1),  # Up / Left and increase both
    (-1, 1),  # Up / Right and increase both
    (1, -1),  # Down / Left and increase both
    (1, 1),  # Down / Right and increase both
]


def check_surround(seats, pos, symbol, around=None):
    seats_around = []

    for check_pos in POSITIONS:
        to_check = [
            check_pos[0] + pos[0],  # X Axis
            check_pos[1] + pos[1],  # Y Axis
        ]

        if to_check[0] < 0 or to_check[1] < 0:
            continue

        try:
            seat = seats[to_check[0]][to_check[1]]
            if seat in (OCCUPIED, SEAT):
                seats_around.append(seat)
                # print(pos, symbol, around, to_check)
        except IndexError:
            continue

    # print(pos, symbol, around, seats_around, depth)

    if not around:
        return all([a == symbol for a in seats_around])

    return seats_around.count(symbol) >= around


def shift_seats(current_map, around):
    new_map = [list(row) for row in current_map]

    for x, row in enumerate(current_map):
        for y in range(len(row)):
            current_seat = current_map[x][y]

            if current_seat == SEAT:
                check_res = check_surround(current_map, [x, y], SEAT)
                # print([x, y], current_seat, check_res, SEAT, OCCUPIED)
                if check_res:
                    new_map[x][y] = OCCUPIED
            elif current_seat == OCCUPIED:
                check_res = check_surround(current_map,
                                           [x, y],
                                           OCCUPIED,
                                           around=around)
                # print([x, y], current_seat, check_res, OCCUPIED, SEAT)
                if check_res:
                    new_map[x][y] = SEAT
            else:
                new_map[x][y] = current_seat

    return ["".join(row) for row in new_map]


def finalize_seats(layout, around):

    while True:
        new_layout = shift_seats(layout, around)
        new_seats = "\n".join(new_layout)

        seats_occupied = new_seats.count(OCCUPIED)
        # print(f"Seats {seats_occupied}\n{new_seats}\n")
        if new_layout == layout:
            return seats_occupied

        layout = new_layout


if __name__ == "__main__":
    testlayout = [line.strip() for line in open("testinput").readlines()]

    seats_found = finalize_seats(testlayout, 4)
    print(f"Found {seats_found} seats found")
    assert seats_found == 37

    # seats_found = finalize_seats(testlayout, 5)
    # print(f"Second Part: found {seats_found} seats found")
    # assert seats_found == 26

    layout = [line.strip() for line in open("input").readlines()]
    seats_found = finalize_seats(layout, 4)
    print(f"Found {seats_found} seats found")
    assert seats_found == 2277
