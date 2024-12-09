# Part 1
# Numbers can be combined with operators to produce the test value.
# For each, there are n-1 possible ones, and so it's (n-1)^2 if we try all
from collections import defaultdict
from enum import Enum
from typing import Dict, Set, Tuple

with open("input.txt", "r") as file:
    lines = file.read().splitlines()

# totalSum = 0
# for line in lines:
#     answer, numbers = line.split(":")
#     # So I want, say for 4 numbers, 3 spots, 000, 001, 010, etc.
#     numbers = numbers.lstrip().rstrip().split(" ")
#     numberOfSlots = len(numbers) - 1
#     for n in range(3**numberOfSlots):
#         combination = bin(n)[2:].zfill(numberOfSlots)
#         currSum = int(numbers[0])
#         for i, number in enumerate(numbers[1:]):
#             if combination[i] == "1":
#                 currSum += int(number)
#             else:
#                 currSum *= int(number)
#         if str(currSum) == answer:
#             print(answer)
#             totalSum += int(answer)
#             print("matched", answer, currSum)
#             break
# # 5030892084481
# print(totalSum)


# Part 2
# new operator ||


def to_base_3(n, length):
    if n == 0:
        return "0" * length
    digits = []
    while n:
        digits.append(str(n % 3))
        n //= 3
    return "".join(reversed(digits)).zfill(length)


totalSum = 0
for line in lines:
    answer, numbers = line.split(":")
    # So I want, say for 4 numbers, 3 spots, 000, 001, 010, etc.
    numbers = numbers.lstrip().rstrip().split(" ")
    numberOfSlots = len(numbers) - 1
    for n in range(3**numberOfSlots):
        combination = to_base_3(n, numberOfSlots)
        currSum = int(numbers[0])
        for i, number in enumerate(numbers[1:]):
            if combination[i] == "1":
                currSum += int(number)
            elif combination[i] == "2":
                currSum *= int(number)
            else:
                currSum = int(str(currSum) + number)
        if str(currSum) == answer:
            print(answer)
            totalSum += int(answer)
            print("matched", answer, currSum)
            break
# 91377448644679
# print(totalSum)
