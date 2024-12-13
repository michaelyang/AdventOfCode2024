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
    def __init__(self, x: int, y: int, plant: str):
        self.x = x
        self.y = y
        self.plant = plant

    def __repr__(self) -> str:
        return f"({self.x}, {self.y})"

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.x == other.x and self.y == other.y


def getNeighbors(coordinate: Coordinate, width, height) -> List[Coordinate | None]:
    neighbors = []
    if coordinate.y > 0:
        # Up
        # print("Up")
        neighbors.append(
            Coordinate(
                coordinate.x, coordinate.y - 1, lines[coordinate.y - 1][coordinate.x]
            )
        )
    else:
        neighbors.append(None)
    if coordinate.x < width - 1:
        # Right
        # print("Right")
        neighbors.append(
            Coordinate(
                coordinate.x + 1, coordinate.y, lines[coordinate.y][coordinate.x + 1]
            )
        )
    else:
        neighbors.append(None)
    if coordinate.y < height - 1:
        # Down
        # print("Down")
        neighbors.append(
            Coordinate(
                coordinate.x, coordinate.y + 1, lines[coordinate.y + 1][coordinate.x]
            )
        )
    else:
        neighbors.append(None)
    if coordinate.x > 0:
        # Left
        # print("Left")
        neighbors.append(
            Coordinate(
                coordinate.x - 1, coordinate.y, lines[coordinate.y][coordinate.x - 1]
            )
        )
    else:
        neighbors.append(None)
    return neighbors


height = len(lines)
width = len(lines[0])


priceSum = 0

visitedCoordinates: Set[Coordinate] = set()

# for y in range(height):
#     for x in range(width):
#         startingCoordinate = Coordinate(x, y)
#         if startingCoordinate in visitedCoordinates:
#             continue
#         plantType = lines[y][x]
#         coordinatesToVisit: List[Coordinate] = [startingCoordinate]
#         area = 0
#         perimeter = 0

#         while coordinatesToVisit:
#             coordinate = coordinatesToVisit.pop()
#             if coordinate in visitedCoordinates:
#                 continue
#             else:
#                 visitedCoordinates.add(coordinate)
#             area += 1
#             neighbors = getNeighbors(coordinate, width, height)
#             for neighbor in neighbors:
#                 if neighbor:
#                     if lines[neighbor.y][neighbor.x] != plantType:
#                         perimeter += 1
#                     if neighbor in visitedCoordinates:
#                         continue
#                     if lines[neighbor.y][neighbor.x] == plantType:
#                         coordinatesToVisit.append(neighbor)
#             if coordinate.x == 0 or coordinate.x == width - 1:
#                 perimeter += 1
#             if coordinate.y == 0 or coordinate.y == height - 1:
#                 perimeter += 1

#         # print("area: ", area)
#         # print("perim: ", perimeter)
#         priceSum += area * perimeter

# # 1319878
# print(priceSum)


# Part 2
# Under the bulk discount, instead of using the perimeter to calculate the price,
# you need to use the number of sides each region has. Each straight section of fence counts as a side, regardless of how long it is.

for y in range(height):
    for x in range(width):
        startingCoordinate = Coordinate(x, y, lines[y][x])
        if startingCoordinate in visitedCoordinates:
            continue
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
            up, right, down, left = getNeighbors(coordinate, width, height)
            # print("considering: ", coordinate)

            # if myself is an edge
            # don't add if left is same edge
            isUpAnEdge = not up or up.plant != startingCoordinate.plant
            isRightAnEdge = not right or right.plant != startingCoordinate.plant
            isDownAnEdge = not down or down.plant != startingCoordinate.plant
            isLeftAnEdge = not left or left.plant != startingCoordinate.plant

            if isUpAnEdge:
                if not left or left.plant != startingCoordinate.plant:
                    isLeftUpASamePlantEdge = False
                else:
                    _up, _right, _down, _left = getNeighbors(left, width, height)
                    isLeftUpASamePlantEdge = not _up or _up.plant != left.plant
                if not isLeftUpASamePlantEdge:
                    perimeter += 1
            if (
                up
                and up not in visitedCoordinates
                and up.plant == startingCoordinate.plant
            ):
                coordinatesToVisit.append(up)

            if isRightAnEdge:
                if not up or up.plant != startingCoordinate.plant:
                    isUpRightASamePlantEdge = False
                else:
                    _up, _right, _down, _left = getNeighbors(up, width, height)
                    isUpRightASamePlantEdge = not _right or _right.plant != up.plant
                if not isUpRightASamePlantEdge:
                    perimeter += 1

            if (
                right
                and right not in visitedCoordinates
                and right.plant == startingCoordinate.plant
            ):
                coordinatesToVisit.append(right)

            if isDownAnEdge:
                if not right or right.plant != startingCoordinate.plant:
                    isRightDownASamePlantEdge = False
                else:
                    _up, _right, _down, _left = getNeighbors(right, width, height)
                    isRightDownASamePlantEdge = not _down or _down.plant != right.plant
                if not isRightDownASamePlantEdge:
                    perimeter += 1
            if (
                down
                and down not in visitedCoordinates
                and down.plant == startingCoordinate.plant
            ):
                coordinatesToVisit.append(down)

            if isLeftAnEdge:
                if not down or down.plant != startingCoordinate.plant:
                    isDownLeftASamePlantEdge = False
                else:
                    _up, _right, _down, _left = getNeighbors(down, width, height)
                    isDownLeftASamePlantEdge = not _left or _left.plant != down.plant
                if not isDownLeftASamePlantEdge:
                    perimeter += 1
            if (
                left
                and left not in visitedCoordinates
                and left.plant == startingCoordinate.plant
            ):
                coordinatesToVisit.append(left)
        # print("area: ", area)
        # print("perim: ", perimeter)
        priceSum += area * perimeter

# 784982
print(priceSum)
