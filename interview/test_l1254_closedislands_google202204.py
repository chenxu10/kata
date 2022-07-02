"""
Given a 2D grid consists of 0s (land) and 1s (water).  
An island is a maximal 4-directionally connected group of 0s 
and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1

Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
"""


def closedIslands(grid):
    # fill island with water using dfs
    # fill island with right, left, up and bottom
    # go through all points in matrix, update solution when it's land and update the soluion
    # fill 0s in left and 0s in right
    m = len(grid)
    n = len(grid[0])

    def dfs(grid, row, col):
        directions = [(-1,0),(1,0),(0,1),(0,-1)]
        if row < 0 or row >= m or col < 0 or col >= n:
            return
        
        if grid[row][col] == 1:
            return

        grid[row][col] = 1
        for x, y in directions:
            dfs(grid, row + x, col + y)
    
    # up and bottom
    for j in range(n):
        dfs(grid, 0, j)
        dfs(grid, m - 1, j)

    # left and right
    for i in range(m):
        dfs(grid, 0, i)
        dfs(grid, i, n - 1)

    res = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                res += 1
                dfs(grid,i,j)
    return res

def test_closedIslands():
    test_matrix_1 = [[0,1,0],[1,0,1],[0,1,0]]
    assert closedIslands(test_matrix_1) == 1

    test_matrix_2 = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
    assert closedIslands(test_matrix_2) == 1

# Related problems number of islands
# Islands means connected zeros