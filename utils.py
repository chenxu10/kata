class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 创建树
def build(data):
    if len(data) == 0:
        return TreeNode(0)
    nodeQueue = []
    # 创建一根节点，并将根节点进栈
    root = TreeNode(data[0])
    nodeQueue.append(root)
    # 记录当前行节点的数量
    lineNum = 2
    # 记录当前行中数字在数组中的位置
    startIndex = 1
    # 记录数组中剩余元素的数量
    restLength = len(data) - 1
    while restLength > 0:
        for index in range(startIndex, startIndex + lineNum, 2):
            if index == len(data):
                return root
            cur_node = nodeQueue.pop()
            if data[index] is not None:
                cur_node.left = TreeNode(data[index])
                nodeQueue.append(cur_node.left)
            if index + 1 == len(data):
                return root
            if data[index + 1] is not None:
                cur_node.right = TreeNode(data[index + 1])
                nodeQueue.append(cur_node.right)
        startIndex += lineNum
        restLength -= lineNum
        # 此处用来更新下一层树对应节点的最大值
        lineNum = len(nodeQueue) * 2
    return root