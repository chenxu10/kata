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
    raise 2

