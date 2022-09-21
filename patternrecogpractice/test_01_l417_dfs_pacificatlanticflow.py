"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. 
The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. 
You are given an m x n integer matrix heights where heights[r][c] represents the 
height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring 
cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes 
that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Mother template should be reachable in digraph from s to v

Given a set of source vertices, is there a path to target vertex
"""

def pacificatlantic(matrix):
    # [1,2,3]
    # [2 3 2]
    # [3 2 2]
    # high > low
    # dfs r,c can flow to the edge
    n = len(matrix)
    m = len(matrix[0])
    canreachpacific = set()
    canreachatlantic = set()

    def dfs(r, c, reachable):
        reachable.add((r, c))
        setoff = [(-1,0),(1,0),(0,-1),(0,1)]
        for x, y in setoff:
            newr = r + x
            newc = c + y
            inBoundary = (newr >=0 and newr < n and newc >=0 and newc < m)
            if inBoundary:
                canFlow = (matrix[newr][newc] >= matrix[r][c])
                notVisited = (newr, newc) not in reachable
                if canFlow and notVisited:
                    dfs(newr, newc, reachable)

    for i in range(n): # left and right
        dfs(i, 0, canreachpacific)
        dfs(i, m - 1, canreachatlantic)

    for j in range(n): # up and down
        dfs(0, j, canreachpacific)
        dfs(n - 1, j, canreachatlantic)

    return list(canreachatlantic & canreachpacific)

def test_pacificatlantic():
    expected = sorted([(0,4),(1,3),(1,4),(2,2),(3,0),(3,1),(4,0)])
    result = sorted(pacificatlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
    assert expected == result

if __name__ == '__main__':
    test_pacificatlantic()

