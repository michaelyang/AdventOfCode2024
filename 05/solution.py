# Part 1
# Safety protocols clearly indicate that new pages for the safety manuals
# must be printed in a very specific order. The notation X|Y means that if
# both page number X and page number Y are to be produced as part of an update,
# page number X must be printed at some point before page number Y.

# page ordering rules and the pages to produce in each update (your puzzle input)
# but can't figure out whether each update has the pages in the right order.


# for | first before second, can be pages between
# 75,47,61,53,29, means that the update consists of page numbers 75, 47, 61, 53, and 29.
# which updates are already in the right order

# Because the first update does not include some page numbers,
# the ordering rules involving those missing page numbers are ignored.

# Take middle of all correctly ordered stuff, then sum

# hmm.... so we need to check all the rules
# naively, take all rules.
# Go through each number:
# 87,63,45,41,37,19,18,88,97,28,89,53,33,22,11,67,34
# 87, check allll rules. n * m where n are numbers of pages being printed and m is number of rules

# sure we can filter the rules by only the applicable ones with the page number being in 2nd col
# but still n * m

# We could also built kinda like a graph, like that phone number problem. If ruleset covers all numbers, it's a bit easier to traverse
# This is probably the most efficient... but I think it's fine.. the input is small

# so we take first number, get all applicable rules.
# Dict of left page number to set of right page numbers
# then we go through all the numbers to the right
# wait, we need the opposite. We need to check if any are VIOLATING
# so dict of right page number to set of left page numbers?
# And if any match, it's violating. so return false.

from collections import defaultdict
from typing import List, Set


pagesThatMustComeBeforeDict: dict[str, set[str]] = defaultdict(set)

with open("input.txt", "r") as file:
    lines = file.read().splitlines()

for line in lines:
    if "|" in line:
        left, right = line.split("|")
        pagesThatMustComeBeforeDict[right].add(left)
# print(pagesThatMustComeBeforeDict)

middleSum = 0

# Getting mid point
# a = "77,32,69,11,94,74,35".split(",")
# print(a[len(a) // 2])


invalidSequences = []
for line in lines:
    if "|" not in line and line != "":
        numbers = line.split(",")
        valid = True
        for i, number in enumerate(numbers):
            pagesThatMustComeBefore = pagesThatMustComeBeforeDict[number]
            # Looking forward
            for nextNumber in numbers[i + 1 :]:
                if nextNumber in pagesThatMustComeBefore:
                    valid = False
                    break
        if valid:
            middleSum += int(numbers[len(numbers) // 2])
        else:
            invalidSequences.append(numbers)
# 5129
# print(middleSum)

# Part 2
# Ok, in hindsight, I should have just done the graph

# Can i just "traverse the graph" using the dict?
# Invalid next nodes are basically the ones that violate the rules
# So..
# 1. List of nodes to visit set [ (1,4,6,8) ]
# 2. Choose a first node, take from nodes to visit 1 [(4,6,8),  ]
# 3. For the next nodes to visit, take the latest set... and check rules again, If any are to be removed, then the sequence is no longer valid.
# 4. If invalid, just pop the set and try the previous one.
# 5. Keep going until all nodes are used and the last set check for singular item is valid.
# 6. Keep going back the set and subtract to build the sequence, or just build it as we go.

middleSumForInvalids = 0
for invalidSequence in invalidSequences:
    # print(invalidSequence)
    setOfNodesToVisit: List[Set[str]] = [set(invalidSequence)]
    currentSequenceAttempt = []

    while len(setOfNodesToVisit) > 0:
        # print("currentSequenceAttempt", currentSequenceAttempt)
        # print("setOfNodesToVisit", setOfNodesToVisit)
        nodesToVisit = setOfNodesToVisit[-1]
        # print("So picking from", nodesToVisit)
        # If set is empty, pop it and try the prev set
        if len(nodesToVisit) == 0:
            setOfNodesToVisit.pop()
            continue

        # This mutates
        nodeToVisit = nodesToVisit.pop()
        # print("picked", nodeToVisit)
        currentSequenceAttempt.append(nodeToVisit)
        if len(currentSequenceAttempt) == len(invalidSequence):
            # print("valid", currentSequenceAttempt)
            # This is a valid sequence, add to sum and break
            middleSumForInvalids += int(
                currentSequenceAttempt[len(currentSequenceAttempt) // 2]
            )
            break
        potentialNodesToVisit = set(invalidSequence) - set(currentSequenceAttempt)
        pagesThatMustComeBefore = pagesThatMustComeBeforeDict[nodeToVisit]
        # print("pagesThatMustComeBefore", pagesThatMustComeBefore)
        if potentialNodesToVisit & pagesThatMustComeBefore:
            currentSequenceAttempt.pop()
        else:
            setOfNodesToVisit.append(potentialNodesToVisit)

print(middleSumForInvalids)
