"""
Prompt:
Suppose an array sorted in ascending order is rotated at some pivot unknown
 to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, 
otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).
"""

# Runs in O(log n) and O(1) space. Checks with (left and mid) and (mid and right)
import math


def search(nums, target):
    left = 0
    right = len(nums) - 1
    while (left <= right):
        mid = math.floor((left + right) / 2)
        if nums[mid] == target:
            return mid
        elif ((nums[left] <= target and target <= nums[mid]) or
              (target <= nums[mid] and nums[mid] < nums[left]) or
              (nums[mid] < nums[left] and nums[left] <= target)):
            right = mid - 1
        else:
            left = mid + 1
    return -1


# Test Case
print(search([4, 5, 6, 7, 0, 1, 2], 1))  # prints 5
