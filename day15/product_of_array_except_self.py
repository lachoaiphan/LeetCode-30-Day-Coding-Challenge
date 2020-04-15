"""
Prompt:
Given an array nums of n integers where n > 1, 
return an array output such that output[i] is equal to the product of all 
the elements of nums except nums[i].
"""

# Runs in O(n) time and O(1) space complexity minus the output array. Used two pointer strategy


def productExceptSelf(nums):
    length = len(nums)
    if length == 0:
        return []
    if length == 1:
        return [0]
    left_prod = nums[0]
    right_prod = nums[length - 1]
    left_index = 1
    right_index = length - 2
    output = [1 for i in range(0, length)]
    while left_index < length and right_index >= 0:
        if left_index == right_index:
            output[left_index] = left_prod * right_prod
        else:
            output[left_index] = output[left_index] * left_prod
            output[right_index] = output[right_index] * right_prod
        left_prod *= nums[left_index]
        right_prod *= nums[right_index]
        left_index += 1
        right_index -= 1
    return output


# Test Cases
print(productExceptSelf([1]))  # Output [0]
print(productExceptSelf([1, 3, 5, 3, 1]))  # Output [45, 15, 9, 15, 45]
print(productExceptSelf([1, 2, 3, 4]))  # Output [24,12,8,6]
