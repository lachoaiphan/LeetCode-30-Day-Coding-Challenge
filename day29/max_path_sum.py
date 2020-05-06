"""
Prompt:
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes 
from some starting node to any node in the tree along the parent-child connections. 
The path must contain at least one node and does not need to go through the root.
"""

# Runs in O(n) time and O(1) space. Set only acquires one maximum number at a time.
# Used four sums to evaluate with each other which is
# Node only, left child with node, right child with node, and all three nodes


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def maxPathSum(root):
    sum_set = set([])
    sum_set.add(-2147483648)
    maxPathSumHelper(root, sum_set)
    return sum_set.pop()


def maxPathSumHelper(root, sum_set):
    if root == None:
        return 0
    left = maxPathSumHelper(root.left, sum_set)
    right = maxPathSumHelper(root.right, sum_set)

    left_sum = left + root.val
    right_sum = right + root.val
    path_sum = max(max(left_sum, right_sum), root.val)

    left_right_sum = max(left + right + root.val, path_sum)

    max_pop = sum_set.pop()
    if max_pop >= left_right_sum:
        sum_set.add(max_pop)
    else:
        sum_set.add(left_right_sum)

    return path_sum


# Test Cases
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.left = node2
node1.right = node3

print(maxPathSum(node1))
