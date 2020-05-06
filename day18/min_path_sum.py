"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""

# Runs in O(n) time and space. Used dynamic programming and minimum function and to
# allocate the lowest available sum for the particular row and column


def minPathSum(grid):
    if len(grid) == 0:
        return 0

    row_length = len(grid)
    col_length = len(grid[0])

    num_paths = [[0 for j in range(0, col_length)]
                 for i in range(0, row_length)]

    num_paths[0][0] = grid[0][0]

    for i in range(1, row_length):
        num_paths[i][0] = num_paths[i - 1][0] + grid[i][0]

    for j in range(1, col_length):
        num_paths[0][j] = num_paths[0][j - 1] + grid[0][j]

    for i in range(1, row_length):
        for j in range(1, col_length):
            num_paths[i][j] = min(num_paths[i - 1][j],
                                  num_paths[i][j - 1]) + grid[i][j]

    return num_paths[row_length - 1][col_length - 1]


# Test Case
min_path = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(minPathSum(min_path))
