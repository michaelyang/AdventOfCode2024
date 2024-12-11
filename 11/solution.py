# Part 1

# If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
# If the stone is engraved with a number that has an even number of digits, it is replaced by two stones.
# The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone.
# (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)

# If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
# No matter how the stones change, their order is preserved, and they stay on their perfectly straight line.

from typing import Dict, List, Set

# When there's a 0, just add it to the count of 0

with open("input.txt", "r") as file:
    lines = file.read().splitlines()


currentStones = lines[0].lstrip().rstrip().split(" ")

stoneSeen: Set[str] = set()


def blink(stones: List[str]) -> List[str]:
    result = []
    for stone in stones:
        stoneSeen.add(stone)
        if ":" in stone:
            number, count = stone.split(":")
            result.append(f"{number}:{int(count)+1}")
        elif stone == "0":
            result.append("1")
        elif len(stone) % 2 == 0:
            leftStone = str(int(stone[: len(stone) // 2]))
            if leftStone in stoneSeen:
                result.append(f"{leftStone}:0")
            else:
                result.append(leftStone)
            rightStone = str(int(stone[len(stone) // 2 :]))
            if rightStone in stoneSeen:
                result.append(f"{rightStone}:0")
            else:
                result.append(rightStone)
        else:
            newStone = str(int(stone) * 2024)
            if newStone in stoneSeen:
                result.append(f"{newStone}:0")
            else:
                result.append(newStone)
    return result


# for _ in range(25):
#     currentStones = blink(currentStones)

# 191690
# print(len(currentStones))

# Part 2
# DP problem with memoize
countDict: Dict[str, int] = {}


# stone is stoneValue:blinkCount
def getStoneCount(stone: str) -> int:
    if stone in countDict:
        return countDict[stone]

    stoneValue, blinkCount = stone.split(":")

    if blinkCount == "0":
        return 1

    if stoneValue == "0":
        count = getStoneCount(f"1:{int(blinkCount)-1}")

    elif len(stoneValue) % 2 == 0:
        leftStone = str(int(stoneValue[: len(stoneValue) // 2]))
        rightStone = str(int(stoneValue[len(stoneValue) // 2 :]))
        count = getStoneCount(f"{rightStone}:{int(blinkCount)-1}") + getStoneCount(
            f"{leftStone}:{int(blinkCount)-1}"
        )
    else:
        newStone = str(int(stoneValue) * 2024)
        count = getStoneCount(f"{newStone}:{int(blinkCount)-1}")
    countDict[stone] = count
    return count


BLINK_COUNT = 75
stonesWithBlinkCount = {f"{stone}:{BLINK_COUNT}" for stone in currentStones}
totalCount = 0
for s in stonesWithBlinkCount:
    totalCount += getStoneCount(s)
# 228651922369703
print(totalCount)
