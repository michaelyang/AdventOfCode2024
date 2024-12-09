# Part 1
# 12345
# 1 id: 0 file
# 2 free space
# 3 id: 1 file
# 4 free space
# 5 id: 2 file
# 0..111....22222

# move file blocks one at a time from the end of the disk to the leftmost free space block
# 0..111....22222
# 02.111....2222.
# 022111....222..
# 0221112...22...
# 02211122..2....
# 022111222......

# 2333133121414131402
# 00...111...2...333.44.5555.6666.777.888899
# 00...111...2...333.44.5555.6666.777.888899
# 009..111...2...333.44.5555.6666.777.88889.
# 0099.111...2...333.44.5555.6666.777.8888..
# 00998111...2...333.44.5555.6666.777.888...
# 009981118..2...333.44.5555.6666.777.88....
# 0099811188.2...333.44.5555.6666.777.8.....
# 009981118882...333.44.5555.6666.777.......
# 0099811188827..333.44.5555.6666.77........
# 00998111888277.333.44.5555.6666.7.........
# 009981118882777333.44.5555.6666...........
# 009981118882777333644.5555.666............
# 00998111888277733364465555.66.............
# 0099811188827773336446555566..............

# Checksum is location * file id summed
from typing import List, Tuple

with open("input.txt", "r") as file:
    lines = file.read().splitlines()
    line = lines[0].rstrip().lstrip()

# print(line)
# Ok, we can just naively make the entire array...
# Probably don't have to though?
# What if we have a dict.
# In the end we want (0, 2), (9,2), (8,1)...
# List of tuples where it's id, length
# Start with (0, 2), (None, 3), (1,3)...
# diskList: List[Tuple[int | None, int]] = []
# charType = "file"
# fileId = 0
# for char in line:
#     if charType == "file":
#         diskList.append((fileId, int(char)))
#         fileId += 1
#         charType = "space"
#     elif charType == "space":
#         diskList.append((None, int(char)))
#         charType = "file"
# print(diskList)

# newDiskList: List[Tuple[int | None, int]] = []
# right = len(diskList) - 1
# for left in range(len(diskList)):
#     if right <= left:
#         break
#     if diskList[left][0] is None:
#         spaceRemaining = diskList[left][1]
#         while spaceRemaining > 0 and right >= left:
#             if diskList[right][0] is None:
#                 right -= 1
#             else:
#                 # Enough space
#                 if diskList[right][1] <= spaceRemaining:
#                     newDiskList.append((diskList[right]))
#                     spaceRemaining -= diskList[right][1]
#                     right -= 1
#                 else:
#                     # Not enough space
#                     newDiskList.append((diskList[right][0], spaceRemaining))
#                     diskList[right] = (
#                         diskList[right][0],
#                         diskList[right][1] - spaceRemaining,
#                     )
#                     spaceRemaining = 0
#     else:
#         newDiskList.append(diskList[left])


def checksum(diskList: List[Tuple[int | None, int]]):
    checksum = 0
    position = 0
    for fileId, length in diskList:
        if fileId is not None:
            for delta in range(length):
                checksum += fileId * (position + delta)
        position += length
    return checksum


# print(newDiskList)
# 6310675819476
# print(checksum(newDiskList))

# Part 2
# Want to move whole files instead
#
# This time, attempt to move whole files to the leftmost span of free space blocks
# that could fit the file. Attempt to move each file exactly once in order of decreasing
# file ID number starting with the file with the highest file ID number.
# If there is no span of free space to the left of a file that is large enough to fit the file, the file does not move.
# 00...111...2...333.44.5555.6666.777.888899
# 0099.111...2...333.44.5555.6666.777.8888..
# 0099.1117772...333.44.5555.6666.....8888..
# 0099.111777244.333....5555.6666.....8888..
# 00992111777.44.333....5555.6666.....8888..

diskList: List[Tuple[int | None, int]] = []
charType = "file"
fileId = 0
for char in line:
    if charType == "file":
        diskList.append((fileId, int(char)))
        fileId += 1
        charType = "space"
    elif charType == "space":
        diskList.append((None, int(char)))
        charType = "file"

# So say we have dictionary to each None block and its size
newDiskList: List[Tuple[int | None, int]] = []
for left in range(len(diskList)):
    right = len(diskList) - 1
    if diskList[left][0] is None:
        availableSpace = diskList[left][1]
        # print(availableSpace)
        while availableSpace > 0 and right >= left:
            # print("LR", left, right)
            if diskList[right][0] is not None and diskList[right][1] <= availableSpace:
                newDiskList.append((diskList[right]))
                availableSpace -= diskList[right][1]
                diskList[right] = (
                    None,
                    diskList[right][1],
                )
                right -= 1
            else:
                right -= 1
        if availableSpace > 0:
            newDiskList.append((None, availableSpace))
    else:
        newDiskList.append(diskList[left])

print(newDiskList)
# 6335972980679
print(checksum(newDiskList))
