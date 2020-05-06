"""
Prompt:
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally
or vertically. 
You may assume all four edges of the grid are all surrounded by water.

"""

# Runs in O(n) and O(n) time and space. Used BFS for each unvisited element


def numIslands(grid):
    visited = []
    islands = 0
    for i in range(0, len(grid)):
        visited.append([False for j in range(0, len(grid[i]))])
    for row in range(0, len(grid)):
        for col in range(0, len(grid[i])):
            if grid[row][col] == "1" and visited[row][col] == False:
                BFS(row, col, visited, grid)
                islands += 1
    return islands


def is_valid(row, col, visited, grid):
    if (row >= 0 and row < len(grid)) and (col >= 0 and col < len(grid[0])):
        return visited[row][col] == False and grid[row][col] == "1"
    return False


def BFS(row, col, visited, grid):
    queue = []
    rows = [-1, 0, 0, 1]
    cols = [0, 1, -1, 0]
    visited[row][col] = True
    queue.append([row, col])
    while len(queue) > 0:
        pair = queue.pop(0)
        cur_row = pair[0]
        cur_col = pair[1]
        for k in range(0, 4):
            if is_valid(cur_row + rows[k], cur_col + cols[k], visited, grid):
                queue.append([cur_row + rows[k], cur_col + cols[k]])
                visited[cur_row + rows[k]][cur_col + cols[k]] = True


# Test Cases
islands = [['1', '1', '0', '0', '0'], ['1', '1', '0', '0', '0'],
           ['0', '0', '1', '0', '0'], ['0', '0', '0', '1', '1']]
print(numIslands(islands))  # prints 3
