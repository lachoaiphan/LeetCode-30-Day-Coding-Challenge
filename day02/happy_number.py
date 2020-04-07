"""
Prompt:
Write an algorithm to determine if a number n is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, 
replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 
(where it will stay), or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.
"""

# Runs in O(k) time and space complexity where k is the amount of times a unique sum has totaled with each iteration.
import math as math


def is_happy(n):
    num_list = []
    next_sum = n
    while True:
        cur_sum = 0
        while (next_sum > 0):
            cur_sum = cur_sum + (pow((next_sum % 10), 2))
            next_sum = math.floor(next_sum / 10)
        if cur_sum == 1:
            return True
        elif cur_sum in num_list:
            return False
        else:
            next_sum = cur_sum
            num_list.append(next_sum)


# Test Cases
print(is_happy(19))  # 19 is a happy number so true

print(is_happy(4))  # 4 is not a happy number so false
