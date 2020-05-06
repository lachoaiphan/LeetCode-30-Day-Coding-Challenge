"""
(This problem is a LeetCode interactive problem meaning that test cases are not available within this file)

A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [rows, cols], which means the matrix is rows * cols.
"""

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

# Runs in O(n log n) time and O(1) space. Uses binary search to search through each row.


def leftMostColumnWithOne(binaryMatrix):
    dimensions = binaryMatrix.dimensions()
    row_length = dimensions[0]
    col_length = dimensions[1]
    row_index = 0
    leftmost_index = col_length
    while row_index < row_length:
        visited = []
        left_index = 0
        right_index = leftmost_index
        while left_index <= right_index:
            mid_index = floor((left_index + right_index) / 2)
            if mid_index in visited:
                break
            mid_value = binaryMatrix.get(row_index, mid_index)
            visited.append(mid_index)
            if mid_value == 1:
                if mid_index < leftmost_index:
                    leftmost_index = mid_index
                right_index = mid_index
            else:
                left_index = mid_index
            row_index += 1
        if leftmost_index == col_length:
            return -1
    return leftmost_index
