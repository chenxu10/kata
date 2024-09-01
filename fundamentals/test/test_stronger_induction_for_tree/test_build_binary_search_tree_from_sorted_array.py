from fundamentals.manbercreativemethod.compute_balancing_factor_07 import sortedArrayToBST

def test_build_height_balanced_tree():
    Node = sortedArrayToBST([-3,0,5,9])
    assert Node.left.val == -3
    assert Node.right.val == 5
    assert Node.right.right.val == 9

    actual = sortedArrayToBST([])
    assert actual == None

if __name__ == "__main__":
    test_build_height_balanced_tree()
