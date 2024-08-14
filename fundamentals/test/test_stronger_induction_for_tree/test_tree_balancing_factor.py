from fundamentals.manbercreativemethod.compute_balancing_factor_07 import compute_balance_factors

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

    # 2. Left-skewed tree
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.left.left = TreeNode(3)
    assert compute_balance_factors(root2) == {1: 2, 2: 1, 3: 0}

    # 3. Right-skewed tree
    root3 = TreeNode(1)
    root3.right = TreeNode(2)
    root3.right.right = TreeNode(3)
    assert compute_balance_factors(root3) == {1: -2, 2: -1, 3: 0}

    # 5. Empty tree
    assert compute_balance_factors(None) == {}

    # 6. Tree with only one node
    root6 = TreeNode(1)
    assert compute_balance_factors(root6) == {1: 0}
