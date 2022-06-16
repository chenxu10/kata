"""
- [] Do you only care about symptoms or can you trace back to several steps
away from the actual fault?  Can you find the root cause of the problem?
Can you find related issues that can be caused by this bug?
- [] Can you reproduce the bug with a single line or 15 steps?
- [] Can you find the root cause of the bugs
"""
                
def sum_roof(root):
    ans = 0
    def preorder(root, curval):
        nonlocal ans
        if root:
            curval = curval * 10 + root.val
            print(curval)
            if (not root.left) and (not root.right):
                ans += curval
            
            preorder(root.left, curval)        
            preorder(root.right, curval)        

    preorder(root, 0)
    return ans

def test_sum_roof_debug1():
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
    assert sum_roof(root) == 1026
    return
