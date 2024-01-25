from collections import deque

"""
You are a hiker preparing for an upcoming hike. You are given heights, 
a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). 
You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, 
(rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.
"""
# 讲清楚左右边界的二分搜索情况

#[[1,2,2],
# [3,8,2],
# [5,3,5]]

# effort (max(x1-y1))

# min(effort)

def bfs(heights, a):
    """
    Reachability
    """
    n = len(heights)
    m = len(heights[0])
    q = deque([(0,0)])
    visited = set()
    steps = 0

    while q:
        row, col = q.popleft()

        for x, y in [(-1,0),(1,0),(0,1),(0,-1)]:
            newx = row + x
            newy = col + y
            inBoundary = (newx > 0 and newx <= n and newy > 0 and newy <= m)
            if inBoundary:
                maxDifference = (heights[newx][newy] - heights[row][col]) <= a
                if ((newx, newy) not in visited) and maxDifference:
                    visited.add((newx, newy))
                    q.append(row, col)
    
    return visited[m - 1][n - 1]           

def binary_search(heights):
    lo = 0
    hi = 1000000

    while lo < hi:
        mid = lo + (hi - lo) // 2
        if bfs(heights, mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


