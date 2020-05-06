"""
Prompt:
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
"""

# Runs in O(n) time and O(1) space. Used a greedy algorithm to evaluate the lowest and highest possible order
# within the string


def checkValidString(s):
    low = 0
    high = 0
    index = 0
    while index < len(s):
        if s[index] == "(":
            low += 1
            high += 1
        elif s[index] == ")":
            if low > 0:
                low -= 1
            high -= 1
        else:
            if low > 0:
                low -= 1
            high += 1
        if high < 0:
            return False
        index += 1
    return low == 0 and high >= 0


# Test Cases
print(checkValidString("(*())"))  # True
print(checkValidString("())"))  # False
print(checkValidString("*((((())))"))  # False
