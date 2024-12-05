# Part 1
# data consist of many reports, one report per line
# 7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9

# each report is a list of levels
# Figure out which reports are safe
# Both true
# 1. all increaisng or all decreasing
# 2. Any two adjacent numbers differ by at least 1 and at most 3

# Just go through report with the logic
with open("input.txt", "r") as file:
    lines = file.read().splitlines()

from enum import Enum
from typing import List


class Direction(Enum):
    INCREASING = 1
    DECREASING = -1


safeReportCount = 0
for report in lines:
    levels = list(map(int, report.split()))

    # Singular levels are always safe
    if len(levels) == 1:
        safeReportCount += 1
        continue

    # If first and last level are the same, it is not safe
    if levels[0] == levels[-1]:
        continue

    # Compare first and last level to get assumed direction
    if levels[0] > levels[-1]:
        direction = Direction.DECREASING
    else:
        direction = Direction.INCREASING

    # Go through each and see if it's safe
    isSafe = True
    previousLevel = levels[0]
    for currentLevel in levels[1:]:
        if currentLevel > previousLevel:
            if direction != Direction.INCREASING:
                isSafe = False
                break
        elif currentLevel < previousLevel:
            if direction != Direction.DECREASING:
                isSafe = False
                break
        else:
            # Equals are not OK
            isSafe = False
            break

        if (
            abs(currentLevel - previousLevel) < 1
            or abs(currentLevel - previousLevel) > 3
        ):
            isSafe = False
            break

        previousLevel = currentLevel
    # If it's safe, add to count
    if isSafe:
        safeReportCount += 1

print(safeReportCount)
# 421


# Part 2
# tolerate a single bad level

# Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.
# Hmm... obviously for each unsafe, we can remove one and try again. that's log(n*m) though...
# what if during the iteration, when we see a bad level, we act as if it wasn't there and move on?
# Then we need to deal with the case where the first level is the bad one or the last level is the bad one...
# def isSafeReport(levels: List[int], allowedBadLevels: int = 0) -> bool:
#     # Singular levels are always safe
#     if len(levels) == 1:
#         return True

#     # If first and last level are the same, it is not safe
#     if levels[0] == levels[-1]:
#         return False

#     # Compare first and last level to get assumed direction
#     if levels[0] > levels[-1]:
#         direction = Direction.DECREASING
#     else:
#         direction = Direction.INCREASING

#     # Go through each and see if it's safe
#     # If we have some allowedBadLevels, minus one and continue. Continuing skips setting prevLevel to current, so just skipping.
#     previousLevel = levels[0]
#     for currentLevel in levels[1:]:
#         if currentLevel > previousLevel:
#             if direction != Direction.INCREASING:
#                 if allowedBadLevels > 0:
#                     allowedBadLevels -= 1
#                     continue
#                 else:
#                     return False
#         elif currentLevel < previousLevel:
#             if direction != Direction.DECREASING:
#                 if allowedBadLevels > 0:
#                     allowedBadLevels -= 1
#                     continue
#                 else:
#                     return False
#         else:
#             if allowedBadLevels > 0:
#                 allowedBadLevels -= 1
#                 continue
#             else:
#                 return False

#         if abs(currentLevel - previousLevel) < 1 or abs(currentLevel - previousLevel) > 3:
#             if allowedBadLevels > 0:
#                 allowedBadLevels -= 1
#                 continue
#             else:
#                 return False
#         previousLevel = currentLevel
#     print(allowedBadLevels)
#     return True

# safeReportCount_2 = 0
# for report in lines:
#     levels = list(map(int, report.split()))
#     if isSafeReport(levels, 1):
#         safeReportCount_2 += 1
#     elif isSafeReport(levels[1:], 0):
#         safeReportCount_2 += 1
#     elif isSafeReport(levels[:-1], 0):
#         safeReportCount_2 += 1
#     else:
#         print(report)
# print(safeReportCount_2)
# ^ this logic falls apart for 1 4 3 4
# 1 4 is valid, but 3 is invalid so we only try not adding 3...
# hmm, just brute force


def isSafeReport(levels: List[int]) -> bool:
    # Singular levels are always safe
    if len(levels) == 1:
        return True
    # If first and last level are the same, it is not safe
    if levels[0] == levels[-1]:
        return False
    # Compare first and last level to get assumed direction
    if levels[0] > levels[-1]:
        direction = Direction.DECREASING
    else:
        direction = Direction.INCREASING

    # Go through each and see if it's safe
    # If we have some allowedBadLevels, minus one and continue. Continuing skips setting prevLevel to current, so just skipping.
    previousLevel = levels[0]
    for currentLevel in levels[1:]:
        if currentLevel > previousLevel:
            if direction != Direction.INCREASING:
                return False
        elif currentLevel < previousLevel:
            if direction != Direction.DECREASING:
                return False
        else:
            return False

        if (
            abs(currentLevel - previousLevel) < 1
            or abs(currentLevel - previousLevel) > 3
        ):
            return False
        previousLevel = currentLevel
    return True


safeReportCount_2 = 0
for report in lines:
    levels = list(map(int, report.split()))
    if isSafeReport(levels):
        safeReportCount_2 += 1
    else:
        for i in range(len(levels)):
            if isSafeReport(levels[:i] + levels[i + 1 :]):
                safeReportCount_2 += 1
                break
print(safeReportCount_2)
# 476
