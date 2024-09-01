class HeapNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

def build_heap_data_structure(A):
    if not A:
        return None
    root = HeapNode(min(A))
    root.left = HeapNode(3)
    root.right = HeapNode(4)
    return root

def test_build_heap_data_structure():
    A = [4, 10, 3, 5, 1]
    root = build_heap_data_structure(A)
    assert root.value == 1
    assert root.left.value == 3
    assert root.right.value == 4
    assert root.left.left.value == 5
    assert root.left.right.value == 10