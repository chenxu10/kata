"""
Extend the induction hypothesis to stronger status, so that reasoning forward
can be easier

The genisus of this chapter is merge sort and we teach how to improve the merge
sort with in-place, top down and bottom up
"""
import copy
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

    def isPowerOfFive(num: int) -> bool:
        while num % 5 == 0:
            num //= 5
        return num == 1

    count = float('inf')
    def backtrack(cur, index):
        nonlocal count
        if index >= len(s):
            count = min(len(cur[:]), count)
            return
        if s[index] == '0':
            return 
            
        for i in range(index, len(s)):
            num = int(s[index:i + 1], 2)
            if isPowerOfFive(num):
                cur.append(s[index:i + 1])
                backtrack(cur, i  + 1)
                cur.pop()

        return count

    backtrack([], 0)

    return count if count != float('inf') else -1

def merge(left,right):
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
 
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge_sort_memory_improve(arr, low, hi):
    """
    """
    def merge_inplace(arr, low, hi, mid):
        # compare [low,mid] with [mid + 1, hi]
        aux = copy.copy(arr)
        i = low
        j = mid + 1
        k = low
        while k <= hi:
            if i > mid + 1:
                arr[k] = aux[j]
                j += 1
            elif j > hi:
                arr[k] = aux[i]
                i += 1
            elif aux[i] < aux[j]:
                arr[k] = aux[i]
                i += 1
            else:
                arr[k] = aux[j]
                j += 1
            k += 1
    if low >= hi:
        return
    mid = (low + hi) // 2
    merge_sort_memory_improve(arr, low, mid)
    merge_sort_memory_improve(arr, mid + 1, hi)
    merge_inplace(arr, low, hi, mid)
    return arr











def getSkyline(buildings: List[List[int]]) -> List[List[int]]:
    def merge_skylines(left, right):
        merged = []
        h1, h2 = 0, 0
        i, j = 0, 0
        
        while i < len(left) and j < len(right):
            x = 0
            if left[i][0] < right[j][0]:
                x, h1 = left[i]
                i += 1
            elif left[i][0] > right[j][0]:
                x, h2 = right[j]
                j += 1
            else:
                x, h1 = left[i]
                _, h2 = right[j]
                i += 1
                j += 1
            
            max_h = max(h1, h2)
            if not merged or max_h != merged[-1][1]:
                merged.append([x, max_h])
        
        merged.extend(left[i:])
        merged.extend(right[j:])
        
        return merged
    
    def helper(buildings):
        if not buildings:
            return []

        if len(buildings) == 1:
            left, right, height = buildings[0]
            return [[left, height], [right, 0]]

        mid = len(buildings) // 2
        left_skyline = helper(buildings[:mid])
        right_skyline = helper(buildings[mid:])

        return merge_skylines(left_skyline, right_skyline)

    return helper(buildings)