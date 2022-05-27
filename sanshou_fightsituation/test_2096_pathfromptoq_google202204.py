"""
You are given the root of a binary tree with n nodes. Each node is uniquely assigned a value from 1 to n. 
You are also given an integer startValue representing the value of the start node s, 
and a different integer destValue representing the value of the destination node t.

Find the shortest path starting from node s and ending at node t. 
Generate step-by-step directions of such path as a string consisting of only 
the uppercase letters 'L', 'R', and 'U'. Each letter indicates a specific direction:

'L' means to go from a node to its left child node.
'R' means to go from a node to its right child node.
'U' means to go from a node to its parent node.
Return the step-by-step directions of the shortest path from node s to node t.

Input: root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
Output: "UURL"
Explanation: The shortest path is: 3 → 1 → 5 → 2 → 6.

"""
def closedIslands():
    # fill island with water using dfs
    # fill island with right, left, up and bottom
    # go through all points in matrix, update solution when it's land and update the soluion
    raise notImplementedError

def test_closedIslands():
    matrix = [[0,1,0],[1,0,1],[0,1,0]]
    assert closedIslands(matrix) == 2