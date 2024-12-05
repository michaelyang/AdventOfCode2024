# Part 1
# xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
# Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

from enum import Enum
from typing import Tuple


with open("input.txt", "r") as file:
    lines = file.read().splitlines()


class MatchingMode(Enum):
    FUNCTION_NAME = 0
    LEFT_PAREN = 1
    ARGS = 2


# so just going from left to right.. see if we see mul
# Once we see that, we check if next is `(`
# if it is, we keep going until we see `)`. If we ever see a non-number or non-comma, we reset (handle special case where it matches the first letter)
# if we see `)`, then we have a match. Try splitting by `,` then verify 2 numbers. mulitply and add
# number wise, idk if 01 is valid. We'll see.
# FUNCTION = "mul"
# STARTING_ARGS: Tuple[MatchingMode, int, str] = (MatchingMode.FUNCTION_NAME, 0, "")

# totalSum = 0
# for line in lines:
#     matchingMode, indexToMatch, argsMatch = STARTING_ARGS
#     for i, letter in enumerate(line):
#         if letter == FUNCTION[0]:
#             matchingMode, indexToMatch, argsMatch = MatchingMode.FUNCTION_NAME, 1, ""
#             continue
#         elif matchingMode == MatchingMode.LEFT_PAREN:
#             if letter == "(":
#                 matchingMode = MatchingMode.ARGS
#             else:
#                 matchingMode, indexToMatch, argsMatch = STARTING_ARGS
#         elif matchingMode == MatchingMode.FUNCTION_NAME:
#             if letter == FUNCTION[indexToMatch]:
#                 indexToMatch += 1
#                 if indexToMatch >= len(FUNCTION):
#                     matchingMode = MatchingMode.LEFT_PAREN
#             else:
#                 matchingMode, indexToMatch, argsMatch = STARTING_ARGS
#         elif matchingMode == MatchingMode.ARGS:
#             if letter == ")":
#                 if argsMatch:
#                     print(argsMatch)
#                     args = argsMatch.split(",")
#                     if len(args) == 2 and args[0].isnumeric() and args[1].isnumeric():
#                         result = int(args[0]) * int(args[1])
#                         # print(f"{args[0]} * {args[1]} = {result}")
#                         totalSum += result
#                 matchingMode, indexToMatch, argsMatch = STARTING_ARGS
#             elif letter in "0123456789,":
#                 argsMatch += letter
#             else:
#                 matchingMode, indexToMatch, argsMatch = STARTING_ARGS
# 178794710
# print(totalSum)

# Part 2
# Ok, i have an idea. It's very hacky, but every iteration, just look at last 4, check if it's equal to `do()`, look at last 7, see if it's equal to `don't()`
# flip enabled flag
FUNCTION = "mul"
STARTING_ARGS: Tuple[MatchingMode, int, str] = (MatchingMode.FUNCTION_NAME, 0, "")

totalSum = 0
# So this comes outside cause it carries over between lines
enabled = True
for line in lines:
    matchingMode, indexToMatch, argsMatch = STARTING_ARGS
    for i, letter in enumerate(line):
        if i >= 5 and line[i - 4 : i] == "do()":
            print(line[i - 4 : i])
            enabled = True
        elif i >= 7 and line[i - 7 : i] == "don't()":
            print(line[i - 7 : i])
            enabled = False

        if letter == FUNCTION[0]:
            matchingMode, indexToMatch, argsMatch = MatchingMode.FUNCTION_NAME, 1, ""
            continue
        elif matchingMode == MatchingMode.LEFT_PAREN:
            if letter == "(":
                matchingMode = MatchingMode.ARGS
            else:
                matchingMode, indexToMatch, argsMatch = STARTING_ARGS
        elif matchingMode == MatchingMode.FUNCTION_NAME:
            if letter == FUNCTION[indexToMatch]:
                indexToMatch += 1
                if indexToMatch >= len(FUNCTION):
                    matchingMode = MatchingMode.LEFT_PAREN
            else:
                matchingMode, indexToMatch, argsMatch = STARTING_ARGS
        elif matchingMode == MatchingMode.ARGS:
            if letter == ")":
                if argsMatch:
                    print(argsMatch)
                    args = argsMatch.split(",")
                    if len(args) == 2 and args[0].isnumeric() and args[1].isnumeric():
                        result = int(args[0]) * int(args[1])
                        # print(f"{args[0]} * {args[1]} = {result}")
                        if enabled:
                            totalSum += result
                matchingMode, indexToMatch, argsMatch = STARTING_ARGS
            elif letter in "0123456789,":
                argsMatch += letter
            else:
                matchingMode, indexToMatch, argsMatch = STARTING_ARGS
# 76729637
print(totalSum)
