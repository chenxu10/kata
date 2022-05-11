"""
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.
"""


"""
# Challenge1:
Try solve it using both preorder recursion and dfs traversal
# Challenge2:
Try maintain a mental graph of trees in your working memory when coding
(Ideas from Simon's minds eye)
"""

def sum_roof(root):
    ans = 0

    def preorder(root, cur_val):
        nonlocal ans
        if root:
            cur_val = cur_val * 10 + root.val
            if (not root.left) and (not root.right):
                ans += cur_val
            preorder(root.left,cur_val)
            preorder(root.right,cur_val)

    preorder(root, 0)
    return ans
    

def test_sum_roof():
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
    
    llroot = TreeNode(val=5)
    lrtoot = TreeNode(val=1)
    leftroot = TreeNode(val=9, left=llroot, right=lrtoot)
    rightroot = TreeNode(val=0)
    root = TreeNode(val=4, left=leftroot, right=rightroot)
    print(sum_roof(root))
    assert sum_roof(root) == 1026
    return
