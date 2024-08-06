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

# Test cases
def test_balance_factors():
    # 1. Perfectly balanced tree
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    assert compute_balance_factors(root1) == {1: 0, 2: 0, 3: 0}

    # # 2. Left-skewed tree
    # root2 = TreeNode(1)
    # root2.left = TreeNode(2)
    # root2.left.left = TreeNode(3)
    # assert compute_balance_factors(root2) == {1: 2, 2: 1, 3: 0}

    # # 3. Right-skewed tree
    # root3 = TreeNode(1)
    # root3.right = TreeNode(2)
    # root3.right.right = TreeNode(3)
    # assert compute_balance_factors(root3) == {1: -2, 2: -1, 3: 0}

    # # 5. Empty tree
    # assert compute_balance_factors(None) == {}

    # # 6. Tree with only one node
    # root6 = TreeNode(1)
    # assert compute_balance_factors(root6) == {1: 0}


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

def main():
    test_balance_factors()
    Node = sortedArrayToBST([-3,0,5,9])
if __name__ == '__main__':
    main()