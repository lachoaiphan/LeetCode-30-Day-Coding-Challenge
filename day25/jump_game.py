"""
Prompt:
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.
"""

# Runs in O(n) and O(1) time and space. Used a greedy algorithm that keeps track of an index containing the maximum number
# and the current index


def canJump(nums):
    nums_len = len(nums) - 1
    max_index = 0
    index = 0
    while index < nums_len and index <= max_index and max_index < nums_len + 1:
        if nums[index] + index > max_index:
            max_index = nums[index] + index
        index += 1
    return max_index >= nums_len


# Test Cases
print(canJump([0, 1]))  # False
print(canJump([2, 3, 1, 1, 4]))  # True
print(canJump([3, 0, 0, 0, 3]))  # False
