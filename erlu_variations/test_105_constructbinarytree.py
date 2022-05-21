class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 创建一二叉树
def createBTree(data, index):
    pNode = None
    if index < len(data):
        if data[index] == None:
            return
        pNode = TreeNode(data[index])
        pNode.left = createBTree(data, 2 * index + 1)
        pNode.right = createBTree(data, 2 * index + 2)
    return pNode

def construct_tree(preorder,inorder):
    raise NotImplementedError

def test_construct_build_tree():
    data = [1,4,9,None,None,15,17]
    expected_node = createBTree(data, 0)
    assert construct_tree([1,4,9,15,17],[4,1,15,9,17]) == expected_node

