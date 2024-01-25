class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.balance_factor = None
        self.height = None

def create_binary_tree(arr, index):
    root = None

    if index < len(arr):
        if arr[index] == None:
            return   
        root = TreeNode(arr[index])
        root.balance_factor = None
        root.left = create_binary_tree(arr, index * 2 + 1)
        root.right = create_binary_tree(arr, index * 2 + 2)

    return root

def get_height(node):
    if node is None:
        return 0
    else:
        if node.height is None:
            node.height = max(get_height(node.left),get_height(node.right))+1
        return node.height

def fill_balance(node):
    if node == None:
        return
    else:
        node.balance_factor = get_height(node.left)-get_height(node.right)
        fill_balance(node.left)
        fill_balance(node.right)
        return

def test_balance_factor():
    arr = [1,4,9,3,6]
    Node = create_binary_tree(arr, 0)
    assert get_height(Node) == 3
    assert get_height(Node.left) == 2
    fill_balance(Node)
    assert Node.balance_factor == 1

if __name__ == '__main__':
    test_balance_factor()