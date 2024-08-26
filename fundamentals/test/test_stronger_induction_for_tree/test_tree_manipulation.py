from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order_traversal(root):
    if not root:
        return

    queue = deque([root])
    result = []

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            if i == level_size - 1:
                result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result

def test_tree_level_order_traversal():
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    print(level_order_traversal(root1))
    assert level_order_traversal(root1) == [1,3]

def main():
    test_tree_level_order_traversal()    

if __name__ == '__main__':
    main()