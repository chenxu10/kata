"""
Extend the induction hypothesis to stronger status, so that reasoning forward
can be easier
"""
from typing import List,Optional

def compute_balance_factors(root):
    """
    balance factors dictioanry

    create a height calculate function
    """
    def calculate_height(root):
        if not root:
            return -1
        else:
            return 1 + max(calculate_height(root.left), calculate_height(root.right))


    def dfs(root):
        if not root:
            return
        
        balancing_factors[root.val] = calculate_height(root.left) - calculate_height(root.right)
        dfs(root.left)
        dfs(root.right)


    balancing_factors = {}
    if not root:
        return balancing_factors   

    dfs(root)
    return balancing_factors

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Leetcode 108, transition from list to trees
    
def sortedArrayToBST(nums: List[int]) -> Optional[TreeNode]:
    def buildBST(left, right):
        if left > right:
            return None
        
        # Find the middle element
        mid = (left + right) // 2
        
        # Create a new node with the middle element
        root = TreeNode(nums[mid])
        # Recursively build left and right subtrees
        root.left = buildBST(left, mid - 1)
        root.right = buildBST(mid + 1, right)
        
        return root

    return buildBST(0, len(nums) - 1)

def generate_subsequence(nums):
    # Advanced related problems combinations and permutations
    def dfs(start, path):
        """
        Reach to the leaf of the recursion tree
        """
        if start == len(nums):
            sol.append(path)
        else:
            # include current node
            dfs(start + 1, path + [nums[start]])
            # not include current node
            dfs(start + 1, path)
            

    sol = []
    path = []
    dfs(0,path)
    return sol


# Backtrack Model
def reachleaf():
    return True

def isvalid(candidates, target):
    return True

def backtrack(candidates, target, s, path, ans):
    if reachleaf():         # reach the leaf node
        ans.append(path[:])
    for i in range(s, len(candidates)):
        if isvalid(candidates, target):
            path.append(candidates[:i + 1])
            backtrack() # adjust candidates, target as problem requires
            path.pop()

def backtrack_substring(s):
    count = float('-inf')

    def isPowerofFive(x):
        while x % 5 == 0:
            num //= 5
        return num == 1                            


    def dfs(cur, index):
        nonlocal count
        if index == len(s):
            count = min(len(cur[:]),count)
            return 
        if s[index] == '0':
            return
        
        for i in range(index, len(s)):
            isPowerofFive(int(s[index:i + 1],2))
            cur.append(s[index:i + 1])
            dfs(cur, i + 1)
            cur.pop()
        return count

    dfs([],0)
    return count if count != float('-inf') else -1