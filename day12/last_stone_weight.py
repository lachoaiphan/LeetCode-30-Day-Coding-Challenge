"""
Prompt:
We have a collection of stones, each stone has a positive integer weight.

Each turn, we choose the two heaviest stones and smash them together.  Suppose the stones have weights x and y with x <= y. 
The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.

At the end, there is at most 1 stone left.  Return the weight of this stone (or 0 if there are no stones left.)
"""

# Runs in O(n log n) time and O(1) space. Sorting the list everytime the weight of two biggest stones are compared


def lastStoneWeight(stones):
    while len(stones) >= 2:
        stones.sort()
        stone1 = stones.pop()
        stone2 = stones.pop()
        if stone1 != stone2:
            stones.append(stone1 - stone2)
    if len(stones) == 0:
        return 0
    elif len(stones) == 1:
        return stones[0]
    raise Exception("More than one stone remain")

# Test Cases


print(lastStoneWeight([]))  # Output 0
print(lastStoneWeight([1, 3]))  # Output 2
print(lastStoneWeight([8, 3, 5]))  # Output 0
print(lastStoneWeight([4, 7, 2, 1, 8, 1]))  # Output 3
