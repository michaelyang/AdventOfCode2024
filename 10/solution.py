# Part 1
# numbers are height
# Based on height, determine good hiking trail
# even, gradual, uphill
# starts at 0, ends at 9, always increase by exactly 1. only up down left right
# What is the sum of the scores of all trailheads on your topographic map?
# score is the number of 9-height positions reachable from that trailhead via a hiking trail
from typing import List, Set


class Coordinate:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.x == other.x and self.y == other.y


def getNeighbors(coordinate: Coordinate, width, height) -> List[Coordinate]:
    neighbors = []
    if coordinate.y > 0:
        # Up
        # print("Up")
        neighbors.append(Coordinate(coordinate.x, coordinate.y - 1))
    if coordinate.x < width - 1:
        # Right
        # print("Right")
        neighbors.append(Coordinate(coordinate.x + 1, coordinate.y))
    if coordinate.y < height - 1:
        # Down
        # print("Down")
        neighbors.append(Coordinate(coordinate.x, coordinate.y + 1))
    if coordinate.x > 0:
        # Left
        # print("Left")
        neighbors.append(Coordinate(coordinate.x - 1, coordinate.y))
    return neighbors


with open("input.txt", "r") as file:
    lines = file.read().splitlines()
height = len(lines)
width = len(lines[0])

startingCoordinates: List[Coordinate] = []

for y in range(height):
    for x in range(width):
        if lines[y][x] == "0":
            startingCoordinates.append(Coordinate(x, y))

scoreSum = 0
ratingSum = 0
for startingCoordinate in startingCoordinates:
    nodesToVisit = [startingCoordinate]
    visitedApex: Set[Coordinate] = set()
    while nodesToVisit:
        node = nodesToVisit.pop()
        currentHeight = int(lines[node.y][node.x])
        if currentHeight == 9:
            ratingSum += 1
            if node not in visitedApex:
                visitedApex.add(node)
        else:
            neighbors = getNeighbors(node, width, height)
            for neighbor in neighbors:
                if lines[neighbor.y][neighbor.x] == str(currentHeight + 1):
                    nodesToVisit.append(neighbor)
    # print(visitedApex)
    scoreSum += len(visitedApex)

# 794
print(scoreSum)
# 1706
print(ratingSum)

# Part 2
# New way to measure rating
# All possible ways to reach top add to rating
# ratingSum above
