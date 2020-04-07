"""
Prompt:

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
input: [-2,1,-3,4,-1,2,1,-5,4]
output: 6
[4,-1,2,1] has the largest sum = 6.
"""

# Finished in O(n) time and O(1) space. Used Silding Window method


def max_subarray(nums):
    max_sum = -2147483648
    cur_sum = -2147483648
    for num in nums:
        cur_sum += num
        if num > cur_sum:
            cur_sum = num
        if cur_sum > max_sum:
            max_sum = cur_sum
    return max_sum


# Test Cases
print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Outputs 6

print(max_subarray([1, 5, -3, 1]))  # Outputs 6
