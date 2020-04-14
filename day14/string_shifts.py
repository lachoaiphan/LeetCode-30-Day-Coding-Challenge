"""
Prompt:
You are given a string s containing lowercase English letters, and a matrix shift, where shift[i] = [direction, amount]:

direction can be 0 (for left shift) or 1 (for right shift). 
amount is the amount by which string s is to be shifted.
A left shift by 1 means remove the first character of s and append it to the end.
Similarly, a right shift by 1 means remove the last character of s and add it to the beginning.

Return the final string after all operations.
 
"""

# Runs in O(n) time and space complexity. Utilized list to string


def stringShift(s, shift):
    str_list = []
    s_length = len(s)
    shift_length = len(shift)
    shift_num = 0
    index = 0
    while index < shift_length:
        if shift[index][0] == 1:
            shift_num -= shift[index][1]
        else:
            shift_num += shift[index][1]
        index += 1
    while len(str_list) < s_length:
        str_list.append(s[shift_num % s_length])
        shift_num += 1
    return ''.join(str_list)


print(stringShift("abc", [[0, 1], [1, 2]]))  # Output cba
print(stringShift("abcdefg", [[1, 1], [1, 1], [0, 2], [1, 3]]))
# Output efgabcd
