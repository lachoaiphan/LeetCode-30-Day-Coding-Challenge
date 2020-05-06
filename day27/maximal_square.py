"""
Prompt:
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
"""

# Runs in O(m * n) time and space with m rows and n columns of the matrix. Uses a dynamic programming algorithm to validate
# nearby values


def maximalSquare(matrix):
    if len(matrix) == 0:
        return 0
    row_len = len(matrix)
    col_len = len(matrix[0])
    squares = [[0 for j in range(0, col_len)] for i in range(0, row_len)]
    max_area = 0
    for j in range(0, col_len):
        squares[0][j] = int(matrix[0][j])
        max_area = max(max_area, squares[0][j])
    for i in range(0, row_len):
        squares[i][0] = int(matrix[i][0])
        max_area = max(max_area, squares[i][0])
    for i in range(1, row_len):
        for j in range(1, col_len):
            if int(matrix[i][j]) == 1:
                squares[i][j] = min(squares[i][j - 1], squares[i - 1][j],
                                    squares[i - 1][j - 1]) + 1
            else:
                squares[i][j] = int(matrix[i][j])
            max_area = max(max_area, squares[i][j])
    return max_area * max_area


# Test Case:
print(maximalSquare([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], [
      "1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]))  # returns 4 as there are squares that makes up 2x2
"""""
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1 
1 0 0 1 0
"""""
