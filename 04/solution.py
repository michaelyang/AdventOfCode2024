# Part 1
# Word Search XMAS
# horizontal, vertical, diagonal, written backwards, or even overlapping other words
# hmm... so for first letter

# XMAS
# MAXS

# What if we just say it's the first letter, and check in all directions? Takes awhile though...
# Input seems small though
# Just make 2d array

from typing import List, Tuple


grid: List[List[str]] = []

with open("input.txt", "r") as file:
    lines = file.read().splitlines()
for line in lines:
    grid.append(list(line))


def getRightN(x: int, y: int, n: int) -> str:
    if x + (n - 1) >= len(grid[0]):
        return ""
    return "".join([grid[y][x + i] for i in range(n)])


def getLeftN(x: int, y: int, n: int) -> str:
    if x - (n - 1) < 0:
        return ""
    return "".join([grid[y][x - i] for i in range(n)])


def getUpN(x: int, y: int, n: int) -> str:
    if y - (n - 1) < 0:
        return ""
    return "".join([grid[y - i][x] for i in range(n)])


def getDownN(x: int, y: int, n: int) -> str:
    if y + (n - 1) >= len(grid):
        return ""
    return "".join([grid[y + i][x] for i in range(n)])


def getQ1DiagonalN(x: int, y: int, n: int) -> str:
    if y - (n - 1) < 0 or x + (n - 1) >= len(grid[0]):
        return ""
    return "".join([grid[y - i][x + i] for i in range(n)])


def getQ2DiagonalN(x: int, y: int, n: int) -> str:
    if y - (n - 1) < 0 or x - (n - 1) < 0:
        return ""
    return "".join([grid[y - i][x - i] for i in range(n)])


def getQ3DiagonalN(x: int, y: int, n: int) -> str:
    if y + (n - 1) >= len(grid) or x - (n - 1) < 0:
        return ""
    return "".join([grid[y + i][x - i] for i in range(n)])


def getQ4DiagonalN(x: int, y: int, n: int) -> str:
    if y + (n - 1) >= len(grid) or x + (n - 1) >= len(grid[0]):
        return ""
    return "".join([grid[y + i][x + i] for i in range(n)])


WORD = "XMAS"
count = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == WORD[0]:
            if getRightN(x, y, len(WORD)) == WORD:
                count += 1
            if getLeftN(x, y, len(WORD)) == WORD:
                count += 1
            if getUpN(x, y, len(WORD)) == WORD:
                count += 1
            if getDownN(x, y, len(WORD)) == WORD:
                count += 1
            if getQ1DiagonalN(x, y, len(WORD)) == WORD:
                count += 1
            if getQ2DiagonalN(x, y, len(WORD)) == WORD:
                count += 1
            if getQ3DiagonalN(x, y, len(WORD)) == WORD:
                count += 1
            if getQ4DiagonalN(x, y, len(WORD)) == WORD:
                count += 1
# 2493
print(count)


# Part 2
def getDiagonals(x: int, y: int) -> Tuple[str, str]:
    if y + 1 >= len(grid) or y - 1 < 0 or x + 1 >= len(grid[0]) or x - 1 < 0:
        return ("", "")
    return (
        "".join([grid[y - 1][x - 1], grid[y][x], grid[y + 1][x + 1]]),
        "".join([grid[y - 1][x + 1], grid[y][x], grid[y + 1][x - 1]]),
    )


count = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == "A":
            diag1, diag2 = getDiagonals(x, y)
            if diag1 in ["MAS", "SAM"] and diag2 in ["MAS", "SAM"]:
                count += 1
# 1890
print(count)
