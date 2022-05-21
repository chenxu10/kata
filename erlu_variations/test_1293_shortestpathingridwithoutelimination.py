from typing import List
from collections import deque
"""
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). 
You can move up, down, left, or right from and to an empty cell in one step.
Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) 
given that you can eliminate at most k obstacles. 
If it is not possible to find such walk return -1.
"""

def shortestPath(grid: List[List[int]], k: int) -> int:
    if len(grid) == 1 and len(grid[0]) == 1:
        return 0
    
    q = deque([(0,0,k,0)])
    visited = set([(0,0,k)])

    if k > (len(grid)-1 + len(grid[0])-1):
        return len(grid)-1 + len(grid[0])-1

    while q:
        row, col, eliminate, steps = q.popleft()
        for new_row, new_col in [(row-1,col), (row,col+1), (row+1, col), (row, col-1)]:
            if (new_row >= 0 and
                new_row < len(grid) and
                new_col >= 0 and
                new_col < len(grid[0])):
                if grid[new_row][new_col] == 1 and eliminate > 0 and \
                    (new_row, new_col, eliminate-1) not in visited:
                    visited.add((new_row, new_col, eliminate-1))
                    q.append((new_row, new_col, eliminate-1, steps+1))
                if grid[new_row][new_col] == 0 and (new_row, new_col, eliminate) not in visited:
                    if new_row == len(grid)-1 and new_col == len(grid[0])-1:
                        return steps+1
                    visited.add((new_row, new_col, eliminate))
                    q.append((new_row, new_col, eliminate, steps+1))

    return -1

def test_shortestPath():
    assert shortestPath([[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1) == 6