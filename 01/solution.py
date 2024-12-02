# Part 1
# unique location ID
# two list side by side, reconcile
# 3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3

# Pair number, how far apart
# Pair smallest on left with smallest on right, so on
# For each pair, add up the distance
# We can sort both lists, compare... 2*nlogn + n
# Can we do better? Does ordering really matter anyways? Why can't I just get difference and add. Cause difference is absolute value.
# Just sorting.

from typing import Dict, List

with open('input.txt', 'r') as file:
    lines = file.readlines()

distanceSum = 0
list1: List[int] = []
list2: List[int] = []

for line in lines:
    num1, num2 = map(int, line.split())
    list1.append(num1)
    list2.append(num2)

for num1, num2 in zip(sorted(list1), sorted(list2)):
    distanceSum += abs(num1 - num2)

print(distanceSum)
# 2580760

# Part 2
# a lot of location IDs appear in both lists
# how often each number from the left list appears in teh right list
# add up each number in the left list after multiplying by the nubmer of times it appears in the right
# so left location id * count(right)

similarityScore = 0
# Make a count dict of right list
dict2: Dict[int, int] = {}
for num in list2:
    dict2[num] = dict2.get(num, 0) + 1
for num in list1:
    similarityScore += num * dict2.get(num, 0)

print(similarityScore)
# 25358365