import logging
from typing import List
from collections import deque
"""
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). 
You can move up, down, left, or right from and to an empty cell in one step.
Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) 
given that you can eliminate at most k obstacles. 
If it is not possible to find such walk return -1.
"""
logger = logging.getLogger()

def shortestPath(grid: List[List[int]], k: int) -> int:
    """
    # minimum steps <=k
    [0 1]
    [1 1] k = 2 1
    """ 

    state = (0,0,k)
    n = len(grid)
    m = len(grid[0])
    q = deque([(0,state)])
    visited = set(state)

    while q:
        steps, state = q.popleft()
        row, col, k  = state
        if (row, col) == (n -1, m -1):
            return steps
        for x, y in [(-1,0),(1,0),(0,-1),(0,1)]:
            newrow = row + x
            newcol = col + y
            if (0 <= newrow < n) and (0 <= newcol < m):
                neweliminations = k - grid[newrow][newcol]
                newstate = (newrow, newcol, neweliminations)
                if neweliminations >= 0 and newstate not in visited:
                    visited.add(newstate)
                    q.append((steps + 1, newstate))

    return -1

def test_shortestPath():
    assert shortestPath([[0,1,1],[0,1,0],[0,1,0]],k = 1) == 4

if __name__ == '__main__':
    test_shortestPath()