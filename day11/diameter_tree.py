"""
Prompt:
Given a binary tree, you need to compute the length of the diameter of the tree. 
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

Example:
          1
         / \
        2   3
       / \     
      4   5    
Outputs 3 as [4, 2, 1, 3] or [5, 2, 1, 3]
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def diameterOfBinaryTree(root) -> int:
    if root == None:
        return 0
    return diameterOfBinaryTreeHelper(root, set([]), 0)


def diameterOfBinaryTreeHelper(root, diameters, index):
    left = 0
    right = 0
    if root.left != None:
        left = 1 + \
            diameterOfBinaryTreeHelper(root.left, diameters, index + 1)
    if root.right != None:
        right = 1 + \
            diameterOfBinaryTreeHelper(root.right, diameters, index + 1)
    if left + right not in diameters:
        diameters.add(left + right)
    if index == 0:
        return max(diameters)
    if left >= right:
        return left
    return right


# Test Case:
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

node1.left = node2
node1.right = node3

node2.left = node4
node2.right = node5

print(diameterOfBinaryTree(node1))  # Output 3

node0 = TreeNode(0)
print(diameterOfBinaryTree(node0))  # Output 0
