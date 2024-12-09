# Part 1
# an antinode occurs at any point that is perfectly in line with two antennas of the same frequency
# So we just go through, find each that are the same freq
# then for each freq, there's n^2 right?
# cause we need n + (n-1) + (n-3) where n is the number of the same freq
# create freq dict of (x, y)

from collections import defaultdict
from typing import Dict, List, Tuple, Set

with open("input.txt", "r") as file:
    lines = file.read().splitlines()
Location = Tuple[int, int]

freqDict: Dict[str, List[Location]] = defaultdict(list)
mapHeight: int = len(lines)
mapWidth: int = len(lines[0])
for y, line in enumerate(lines):
    for x, freq in enumerate(line.rstrip().lstrip()):
        if freq != ".":
            freqDict[freq].append((x, y))

antinodes: Set[Location] = set()
# print(freqDict)
# print(mapHeight, mapWidth)
# for freq, nodes in freqDict.items():
#     for i, node in enumerate(nodes):
#         for otherNode in nodes[i + 1 :]:
#             xDelta = abs(int(otherNode[0]) - int(node[0]))
#             yDelta = abs(int(otherNode[1]) - int(node[1]))
#             if node[0] < otherNode[0]:
#                 antinode1X = int(node[0]) - xDelta
#                 antinode2X = int(otherNode[0]) + xDelta
#             else:
#                 antinode1X = int(node[0]) + xDelta
#                 antinode2X = int(otherNode[0]) - xDelta

#             if node[1] < otherNode[1]:
#                 antinode1Y = int(node[1]) - yDelta
#                 antinode2Y = int(otherNode[1]) + yDelta
#             else:
#                 antinode1Y = int(node[1]) + yDelta
#                 antinode2Y = int(otherNode[1]) - yDelta

#             if (
#                 antinode1X >= 0
#                 and antinode1Y >= 0
#                 and antinode1X < mapHeight
#                 and antinode1Y < mapWidth
#             ):
#                 antinodes.add((antinode1X, antinode1Y))
#             if (
#                 antinode2X >= 0
#                 and antinode2Y >= 0
#                 and antinode2X < mapHeight
#                 and antinode2Y < mapWidth
#             ):
#                 antinodes.add((antinode2X, antinode2Y))

# 285
# print(len(antinodes))

# Part 2
# antinodes actually occur at any grid position
# exactly in line with at least two antennas of the same frequency, regardless of distance

for freq, nodes in freqDict.items():
    for i, node in enumerate(nodes):
        for otherNode in nodes[i + 1 :]:
            xDelta = int(otherNode[0]) - int(node[0])
            yDelta = int(otherNode[1]) - int(node[1])
            print(xDelta, yDelta)
            # Add self
            newX = int(node[0])
            newY = int(node[1])
            while newX >= 0 and newY >= 0 and newX < mapHeight and newY < mapWidth:
                antinodes.add((newX, newY))
                newX += xDelta
                newY += yDelta

            newX = int(otherNode[0])
            newY = int(otherNode[1])
            while newX >= 0 and newY >= 0 and newX < mapHeight and newY < mapWidth:
                antinodes.add((newX, newY))
                newX -= xDelta
                newY -= yDelta
print(antinodes)
# 944
print(len(antinodes))
