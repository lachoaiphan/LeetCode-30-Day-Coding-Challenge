"""
Prompt:
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
"""

# Finished in O(n) time and O(1) space. Implemented two pointer strategy


def move_zeroes(nums):
    if (len(nums) == 0):
        returnb
    left_index = 0
    right_index = 0
    while (right_index < len(nums)):
        if (nums[right_index] != 0):
            swap(nums, left_index, right_index)
            left_index += 1
        right_index += 1


def swap(nums, left, right):
    temp = nums[left]
    nums[left] = nums[right]
    nums[right] = temp


# Test Cases
nums1 = [0, 1, 0, 3, 12]
move_zeroes(nums1)
print(nums1)  # Outputs [1, 3, 12, 0, 0]

nums2 = [0, 0, 0, 0, 8, 2, 0, 0]
move_zeroes(nums2)
print(nums2)  # Outputs [8, 2, 0, 0, 0, 0, 0, 0]
