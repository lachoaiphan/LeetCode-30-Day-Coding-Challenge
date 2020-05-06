"""
Prompt:
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
"""

# Runs in O(n) time and space. Implemented a hash table to store the cumulative sum with the amount of occurrences throughout the array.
# Checks to see if the complement of the current sum and the target is found then there is a subarray amounting to k.


def subarraySum(nums, k):
    sum_dict = {0: 1}
    total_sum = 0
    count = 0
    nums_len = len(nums)
    for index in range(0, nums_len):
        total_sum += nums[index]
        complement = total_sum - k
        if complement in sum_dict:
            count += sum_dict[complement]
        if total_sum not in sum_dict:
            sum_dict[total_sum] = 1
        else:
            sum_dict[total_sum] += 1
    return count


# Test Cases:
print(subarraySum([1, 1, 1], 2))  # prints 2
