def meeting_planner(slotsA, slotsB, dur):
    length_a = len(slotsA)
    length_b = len(slotsB)

    i = 0
    j = 0

    while i < length_a and j < length_b:
        a = slotsA[i]
        b = slotsB[j]
        if a[1] - a[0] < dur:
            i += 1
            continue
        if b[1] - b[0] < dur:
            j += 1
            continue
        overlapped = min(a[1], b[1]) - max(a[0], b[0])
        if overlapped >= dur:
            return [max(a[0], b[0]), max(a[0], b[0]) + dur]
        elif a[1] < b[1]:
            i += 1
        else:
            j += 1
    return []


slotsA = [[10, 50], [60, 120], [140, 210]]
slotsB = [[0, 15], [60, 70]]
dur = 8

print(meeting_planner(slotsA, slotsB, dur))

slotsA = [[10, 50], [60, 120], [140, 210]]
slotsB = [[0, 15], [60, 70]]
dur = 12

slotsA = [[7, 12]]
slotsB = [[2, 11]]
dur = 5

slotsA = [[1, 10]]
slotsB = [[2, 3], [5, 7]]
dur = 2

print(meeting_planner(slotsA, slotsB, dur))

# your code goes here
# Epoch time.
# [10, 50], [60,120]
# Sorted
# earliest
# disjointed