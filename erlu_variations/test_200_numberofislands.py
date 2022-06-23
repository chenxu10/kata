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

# juzhen laping
# class UnionCount():
from collections import defaultdict

class UnionFind():
    # construct
    def __init__(self, numElements):
        self.parent = [i for i in range(numElements)]

    def find(self,x):
        if (self.parent[x] == x):
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, p, q):
        rootx = self.find(p)
        rooty = self.find(q)
        if rootx == rooty:
            return False
        self.parent[rootx] = rooty
        return True

    # count
    def count(self):
        return self.count()

def numberofIslands(grid):
    """
    Returns a count
    """
    m = len(grid)
    n = len(grid[0])
    UF = UnionFind(m * n)
    count = 0
    offset = [(-1,0),(1,0),(0,1),(0,-1)]

    def unionround(grid, x, y):
        nonlocal count
        mark = x * n + y
        for dirx, diry in offset:
            newx = x + dirx
            newy = y + diry
            inbound = (newx >= 0 and newx < m and newy >= 0 and newy < n and grid[newx][newy] == '1')
            if inbound:
                if UF.union(newx * n + newy, mark):
                    count -= 1

    for x in range(m):
        for y in range(n):
            if grid[x][y] == "1":
                count += 1
                unionround(grid, x, y)
    
    return count

# Follow up questions leetcode 305


def test_numberofIslands():
    grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
    ]
    print(numberofIslands(grid))
    assert numberofIslands(grid) == 3

if __name__ == '__main__':
    test_numberofIslands()