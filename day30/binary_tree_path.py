"""
Prompt:
Given a binary tree where each path going from the root to any leaf form a valid sequence, 
check if a given string is a valid sequence in such binary tree. 

We get the given string from the concatenation of an array of integers arr
 and the concatenation of all values of the nodes along a path results in a sequence in the given binary tree.
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

# Runs in O(n) time and space. Recursive solution to validate each node


def isValidSequence(root, arr):
    return isVSHelper(root, arr, 0)


def isVSHelper(root, arr, pos):
    if root == None:
        return False
    if root.val == arr[pos]:
        if pos + 1 >= len(arr):
            return root.left == None and root.right == None
        left = False
        right = False
        if root.left != None:
            left = isVSHelper(root.left, arr, pos + 1)
        if root.right != None:
            right = isVSHelper(root.right, arr, pos + 1)
        return left or right
    return False


# Test Case
node1 = TreeNode(0)
node2 = TreeNode(2)
node3 = TreeNode(4)
node4 = TreeNode(4)

node1.right = node2
node2.right = node3

print(isValidSequence(node1, [0]))  # False
print(isValidSequence(node1, [0, 4]))  # False
node1.left = node4
print(isValidSequence(node1, [0, 4]))  # True
print(isValidSequence(node1, [0, 2]))  # False
print(isValidSequence(node1, [0, 2, 4]))
