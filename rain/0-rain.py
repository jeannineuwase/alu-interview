#!/usr/bin/python3
"""calculate water retained"""


def rain(walls):
    total_water_retained = 0
    start_index = None
    end_index = None
    limit = len(walls)

    i = 0
    while i < limit:
        next_wall_height = 0
        if i + 1 < limit:
            next_wall_height = walls[i + 1]

        if start_index is not None and end_index is not None:
            smallest_wall_height = min(walls[start_index], walls[end_index])
            for wall_index in range(start_index + 1, end_index):
                total_water_retained += smallest_wall_height - walls[wall_index]
            start_index = None
            end_index = None

        if start_index is None and walls[i] > 0:
            start_index = i
            i += 1
            continue

        if start_index is not None and walls[i] > walls[i - 1] and walls[i] >= next_wall_height:
            end_index = i
            continue

        i += 1

    return total_water_retained
