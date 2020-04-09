"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.
"""

# Runs in O(n) time and O(S + T) space. Implemented stacks to compare the two strings


def backspace_compare(S, T):
    stack1 = []
    stack2 = []
    index = 0
    while index < len(S) or index < len(T):
        if index < len(S):
            if S[index] == '#':
                if len(stack1) > 0:
                    stack1.pop()
            else:
                stack1.append(S[index])
        if index < len(T):
            if T[index] == '#':
                if len(stack2) > 0:
                    stack2.pop()
            else:
                stack2.append(T[index])
        index += 1
    while len(stack1) > 0 and len(stack2) > 0:
        if stack1.pop() != stack2.pop():
            return False
    return len(stack1) == 0 and len(stack2) == 0


# Test Cases
print(backspace_compare("ab#c", "ad#c"))  # return True

print(backspace_compare("a#c", "b"))  # return False
