# Part 1

# region area and perimeter
# area is number of garden plots
# Foursides, so perimeter just add sides

# price is area * perimeter for each region


# Floodfill, get region, calculate, add

from typing import List, Set


with open("input.txt", "r") as file:
    lines = file.read().splitlines()


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


height = len(lines)
width = len(lines[0])


priceSum = 0

visitedCoordinates: Set[Coordinate] = set()

for y in range(height):
    for x in range(width):
        startingCoordinate = Coordinate(x, y)
        if startingCoordinate in visitedCoordinates:
            continue
        plantType = lines[y][x]
        coordinatesToVisit: List[Coordinate] = [startingCoordinate]
        area = 0
        perimeter = 0

        while coordinatesToVisit:
            coordinate = coordinatesToVisit.pop()
            if coordinate in visitedCoordinates:
                continue
            else:
                visitedCoordinates.add(coordinate)
            area += 1
            neighbors = getNeighbors(coordinate, width, height)
            for neighbor in neighbors:
                if lines[neighbor.y][neighbor.x] != plantType:
                    perimeter += 1
                if neighbor in visitedCoordinates:
                    continue
                if lines[neighbor.y][neighbor.x] == plantType:
                    coordinatesToVisit.append(neighbor)
            if coordinate.x == 0 or coordinate.x == width - 1:
                perimeter += 1
            if coordinate.y == 0 or coordinate.y == height - 1:
                perimeter += 1

        # print("area: ", area)
        # print("perim: ", perimeter)
        priceSum += area * perimeter

# 1319878
print(priceSum)
