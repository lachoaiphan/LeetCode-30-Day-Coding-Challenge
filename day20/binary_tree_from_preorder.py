class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def printTreeNodes(root):
    if root == None:
        return
    print(root.val)
    printTreeNodes(root.left)
    printTreeNodes(root.right)


"""
Prompt:
Return the root node of a binary search tree that matches the given preorder traversal.

(Recall that a binary search tree is a binary tree where for every node, 
any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  
Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)

It's guaranteed that for the given test cases there is always possible to find a binary search tree with the given requirements.
"""

# Runs in O(n) time and space. Iterative solution to make a list version of the tree in a preorder fashion


def bstFromPreorder(preorder):
    if len(preorder) == 0:
        return None
    root = TreeNode(preorder[0])
    node_list = [root]
    index = 1
    length = len(preorder)
    while index < length:
        cur_node = TreeNode(preorder[index])
        cur_index = 0
        while True:
            cur_root = node_list[cur_index]
            if cur_root.val > cur_node.val:
                if cur_root.left == None:
                    cur_root.left = cur_node
                    node_list.append(cur_node)
                    break
                else:
                    cur_index = node_list.index(node_list[cur_index].left)
            else:
                if cur_root.right == None:
                    cur_root.right = cur_node
                    node_list.append(cur_node)
                    break
                else:
                    cur_index = node_list.index(node_list[cur_index].right)
        index += 1
    return root


# Test Case
node1 = bstFromPreorder([8, 5, 1, 7, 10, 12])
printTreeNodes(node1)
