"""
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.
"""

"""
# Challenge1:
Try solve it using both 
preorder recursion
-iterative
-recursive
-morris
dfs traversal
preorder traversal
bfs traversal 
# Challenge2:
Try maintain a mental graph of trees in your working memory when coding
(Ideas from Simon's minds eye)
# Challenge3:
No backspace while typing solution from beginning to end
# Challenge4:
Can you find the root cause of the bug
# Challenge5:
Can you describe the algorithm
# Challenge6:
Can you parse the problems into 4-5 chunks you can manage
# Challenge6:
Can you make your mind not switching back and forth between different levels
- function level to indentation level
# Challenge7:
- Debugging: 
- Read error messge
- Don't focus on symptoms, find several steps ahead of
symptoms and dig deep into root causwes
# Challenge8:
"""

# You will first need to understand morris traversal
# https://www.thealgorists.com/Algo/Tree/MorrisPreorder

def sum_roof_dynamic_programming(root):

    def helper(root, ans=0):
        """
        Sum of roof connecting to all left part or right part
        containing all root
        """
        if not root:
            return 0
        if root:
            ans = ans * 10 + root.val
            if (not root.left) and (not root.right):
                return ans
                
        return helper(root.left, ans) + helper(root.right, ans)

    return helper(root, 0)

def sum_roof_backtrack_traverse(root):
    ans = 0
    paths = []

    def dfs(node):
        nonlocal ans
        def path_sum(paths):
            return int("".join([str(i) for i in paths]))
        if node:
            paths.append(node.val)
            if not (node.left or node.right):
                ans += path_sum(paths)
            dfs(node.left)
            dfs(node.right)
            paths.pop() # postorder
    
    dfs(root)
    return ans

def sum_roof_dfs_iterative(root):

    def dfs(node, stack):
        ans = 0
        while stack:
            node, cur_num = stack.pop()
            if node:
                cur_num = cur_num * 10 + node.val
                if not (node.left or node.right):
                    ans += cur_num
                else:
                    stack.append((node.left,cur_num))
                    stack.append((node.right, cur_num))
        return ans

    stack = [(root,0)]
    ans = dfs(root, stack)
    
    return ans

# BFS iterative solution
def sum_roof_bfs_iterative(root):
    
    def bfs(node,q):
        ans = 0
        while q:
            node, cur_num = q.pop(0)
            if node:
                cur_num = cur_num * 10 + node.val
                if not (node.left or node.right):
                    ans += cur_num
                else:
                    q.append((node.left,cur_num))
                    q.append((node.right, cur_num))
        return ans

    q = [(root,0)]
    ans = bfs(root,q=q)
    return ans
    
# BFS recursive solution
def sum_roof_bfs_recursive(root):
    ans = 0
    def bfs(root):
        nonlocal ans
        if not root:
            return
        if not (root.left or root.right):
            ans += root.val
        if root.left:
            root.left.val = root.val * 10 + root.left.val
            bfs(root.left)
        if root.right:
            root.right.val = root.val * 10 + root.right.val
            bfs(root.right)
    bfs(root)
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
    assert sum_roof_dfs_iterative(root) == 1026
    return
