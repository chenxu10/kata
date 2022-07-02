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
from typing import Optional

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
  def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
    def lca(root: Optional[TreeNode]) -> Optional[TreeNode]:
      if not root or root.val in (startValue, destValue):
        return root
      l = lca(root.left)
      r = lca(root.right)
      if l and r:
        return root
      return l or r

    def dfs(root: Optional[TreeNode], path: List[chr]) -> None:
      if not root:
        return
      if root.val == startValue:
        self.pathToStart = ''.join(path)
      if root.val == destValue:
        self.pathToDest = ''.join(path)
      path.append('L')
      dfs(root.left, path)
      path.pop()
      path.append('R')
      dfs(root.right, path)
      path.pop()

    dfs(lca(root), [])  # only this subtree matters
    return 'U' * len(self.pathToStart) + ''.join(self.pathToDest)

# Prerequisites:
# L236. (Lowest Common Ancestor of a Binary Tree)

