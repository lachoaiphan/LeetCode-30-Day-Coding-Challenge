"""
Prompt:
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.
"""

# Runs in O(n) time and space complexity. Implemented hash table using count as key and index as value


def findMaxLength(nums):
    num_dict = {0: -1}  # (count, index)
    count = 0
    max_len = 0
    for index in range(0, len(nums)):
        if nums[index] == 1:
            count += 1
        else:
            count -= 1
        if count not in num_dict:
            num_dict[count] = index
        elif index - num_dict[count] > max_len:
            max_len = index - num_dict[count]
    return max_len


# Test Cases
print(findMaxLength([1, 0, 0, 1]))  # Output 4
# Output 2 as [1, 0] or [0, 1] will be accepted as subarrays
print(findMaxLength([1, 0, 0, 0, 1]))
