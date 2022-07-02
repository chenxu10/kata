"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes 
in the tree.

According to the definition of LCA on Wikipedia: 
“The lowest common ancestor is defined between two nodes p and q as the lowest node 
in T that has both p and q as descendants (where we allow a node to be a descendant 
of itself).”


Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':       
        if not root:
            return None
        if root == p or root == q:
            return root

        # Look for keys in left and right subtrees
        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)

        # If both of the above calls return Non-NULL, then one key
        # is present in once subtree and other is present in other,
        # So this node is the LCA
        if left_lca and right_lca:
            return root

        # Otherwise check if left subtree or right subtree is LCA
        return left_lca if left_lca is not None else right_lca