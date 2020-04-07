"""
Prompt:
Given an integer array arr, count element x such that x + 1 is also in arr.

If there're duplicates in arr, count them seperately.
"""

# Runs in O(n) time and space complexity. Uses a hash set implementation


def count_elements(arr):
    num_set = set([])
    count = 0
    for num in arr:
        if num not in num_set:
            if num + 1 in arr:
                num_set.add(num)
                count += 1
        else:
            count += 1
    return count


# Test Cases
print(count_elements([1, 2, 3]))  # Outputs 2

print(count_elements([1, 1, 2]))  # Outputs 2

print(count_elements([1, 3, 2, 3, 5, 0]))  # Outputs 3

print(count_elements([1, 1, 3, 3, 5, 5, 7, 7]))  # Outputs 0
