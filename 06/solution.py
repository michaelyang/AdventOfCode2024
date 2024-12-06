# Part 1
# Grid, # are shown as obstacles
# Direction. If something infront, turn right, otherwise move fowrard
# Count the number of distinct positions they will visit

# so it's just cycle detection. if already visited and facing same direction, then we're done.
# If they leave the map, they're done.

from collections import defaultdict
from enum import Enum
from typing import Dict, Set, Tuple


class Direction(Enum):
    UP = "^"
    RIGHT = ">"
    DOWN = "v"
    LEFT = "<"


# Reverse mapping from character to Direction enum
charToDirectionMap = {direction.value: direction for direction in Direction}

# obstacles: Set[Tuple[int, int]] = set()
# guardPosition: Tuple[int, int] = (0, 0)
# guardDirection: Direction = Direction.UP

# with open("input.txt", "r") as file:
#     lines = file.read().splitlines()

# for y, line in enumerate(lines):
#     for x, char in enumerate(line):
#         if char == "#":
#             obstacles.add((x, y))
#         elif char in charToDirectionMap:
#             guardPosition = (x, y)
#             guardDirection = charToDirectionMap[char]

# visitedPositions: Dict[Tuple[int, int], set[Direction]] = defaultdict(set)
# # Top left is 0,0
# # Bottom left is 0, len(lines)
# # Top right is len(lines[0]), 0
# # Bottom right is len(lines[0]), len(lines)
# while (
#     guardDirection not in visitedPositions.get(guardPosition, set())
#     and guardPosition[0] >= 0
#     and guardPosition[0] < len(lines[0])
#     and guardPosition[1] >= 0
#     and guardPosition[1] < len(lines)
# ):
#     visitedPositions[guardPosition].add(guardDirection)
#     if guardDirection == Direction.UP:
#         potentialGuardPosition = (guardPosition[0], guardPosition[1] - 1)
#     elif guardDirection == Direction.RIGHT:
#         potentialGuardPosition = (guardPosition[0] + 1, guardPosition[1])
#     elif guardDirection == Direction.DOWN:
#         potentialGuardPosition = (guardPosition[0], guardPosition[1] + 1)
#     elif guardDirection == Direction.LEFT:
#         potentialGuardPosition = (guardPosition[0] - 1, guardPosition[1])

#     if potentialGuardPosition in obstacles:
#         if guardDirection == Direction.UP:
#             guardDirection = Direction.RIGHT
#         elif guardDirection == Direction.RIGHT:
#             guardDirection = Direction.DOWN
#         elif guardDirection == Direction.DOWN:
#             guardDirection = Direction.LEFT
#         elif guardDirection == Direction.LEFT:
#             guardDirection = Direction.UP
#     else:
#         guardPosition = potentialGuardPosition

# 4778
# print(len(visitedPositions.keys()))

# Part 2
# Ok, same logic, just need to try putting obstable in every position and see if there's a cycle
# It doesn't really matter what you choose to use as an obstacle so long as you and The Historians can put it into position without the guard noticing.
# the new obstruction can't be placed at the guard's starting position

obstacles: Set[Tuple[int, int]] = set()
startingGuardPosition: Tuple[int, int] = (0, 0)
startingGuardDirection: Direction = Direction.UP
possibleObstacles: Set[Tuple[int, int]] = set()

with open("input.txt", "r") as file:
    lines = file.read().splitlines()

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == "#":
            obstacles.add((x, y))
        elif char in charToDirectionMap:
            startingGuardPosition = (x, y)
            startingGuardDirection = charToDirectionMap[char]
        else:
            possibleObstacles.add((x, y))

count = 0
for possibleObstacle in possibleObstacles:
    print(f"Trying {possibleObstacle}")
    obstacles.add(possibleObstacle)
    isCycle = False
    visitedPositions: Dict[Tuple[int, int], set[Direction]] = defaultdict(set)
    guardPosition = startingGuardPosition
    guardDirection = startingGuardDirection

    while (
        guardPosition[0] >= 0
        and guardPosition[0] < len(lines[0])
        and guardPosition[1] >= 0
        and guardPosition[1] < len(lines)
    ):
        # This is a cycle now
        if guardDirection in visitedPositions.get(guardPosition, set()):
            isCycle = True
            break

        visitedPositions[guardPosition].add(guardDirection)
        if guardDirection == Direction.UP:
            potentialGuardPosition = (guardPosition[0], guardPosition[1] - 1)
        elif guardDirection == Direction.RIGHT:
            potentialGuardPosition = (guardPosition[0] + 1, guardPosition[1])
        elif guardDirection == Direction.DOWN:
            potentialGuardPosition = (guardPosition[0], guardPosition[1] + 1)
        elif guardDirection == Direction.LEFT:
            potentialGuardPosition = (guardPosition[0] - 1, guardPosition[1])
        else:
            raise Exception("Invalid direction")

        if potentialGuardPosition in obstacles:
            if guardDirection == Direction.UP:
                guardDirection = Direction.RIGHT
            elif guardDirection == Direction.RIGHT:
                guardDirection = Direction.DOWN
            elif guardDirection == Direction.DOWN:
                guardDirection = Direction.LEFT
            elif guardDirection == Direction.LEFT:
                guardDirection = Direction.UP
        else:
            guardPosition = potentialGuardPosition
    if isCycle:
        count += 1
    obstacles.remove(possibleObstacle)
# 1618
print(count)
