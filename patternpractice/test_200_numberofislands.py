"""
You are given an empty 2D binary grid grid of size m x n. 
The grid represents a map where 0's represent water and 1's represent land. 
Initially, all the cells of grid are water cells (i.e., all the cells are 0's).

We may perform an add land operation which turns the water at position into a land. 
You are given an array positions where positions[i] = [ri, ci] is the position (ri, ci) at which we should operate the ith operation.

Return an array of integers answer where answer[i] is the number of islands after turning the cell (ri, ci) into a land.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Input: m = 3, n = 3, positions = [[0,0],[0,1],[1,2],[2,1]]
Output: [1,1,2,3]
"""

# [1,1,1,2,2,3]
#  1 2 3 4 5 6

#     3     5
#   2     4
# 1
#4
#10

# find_parent(1) == find_parent(2)


# juzhen laping
# class UnionCount():
class UnionFound:
    def __init__(self,N):
        self.parent = [i for i in range(N)]

    def find_parent(self, x):
        if x == self.parent[x]:
            return x
        else:
            self.parent[x] = self.find_parent(self.parent[x]) # path compression
            return self.parent[x]

    def union(self, p, q):
        rootp = self.find_parent(p)
        rootq = self.find_parent(q)
        if rootp == rootq:
            return False
        self.parent[rootp] = rootq
        return True

def numberofIslands(grid):
    """
    Returns a count
    """
    n = len(grid)
    m = len(grid[0])
    count = 0
    offset = [(-1,0), (1,0), (0,-1), (0,1)]
    UF = UnionFound(n * m)
    # iteratre through grid, add 1 

    def unionisland(grid, x, y):
        nonlocal count
        index = x * n + y
        for dirx, diry in offset:
            newx = x + dirx
            newy = y + diry
            inboundary = (
            newx >= 0 and newx < n 
            and newy >= 0 and newy < m 
            and grid[newx][newy]=="1")
            if inboundary:
                newindex = newx * n + newy
                if UF.union(index, newindex):
                    count -= 1 

    for x in range(n):
        for y in range(m):
            if grid[x][y] == "1":
                count += 1
                unionisland(grid, x, y)

    return count

# Challenges: Try to solve it in DFS manner
# Challenges: Try to solve problems 305

def test_numberofIslands():
    grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]
    grid2 = [
    ["1","1","0","1","0"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]
    print(numberofIslands(grid))
    assert numberofIslands(grid) == 3
    print(numberofIslands(grid2))
    assert numberofIslands(grid2) == 5

if __name__ == '__main__':
    test_numberofIslands()