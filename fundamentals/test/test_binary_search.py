# Mistakes you made implement this algo
# mid, empty space return -1
from typing import Generic, TypeVar, Optional, Iterable
from collections import deque

Key = TypeVar('Key')
Value = TypeVar('Value')

def binary_search(A,x):
    def recursive_search(low,high):
        if low > high:
            return -1
        mid = (low + high) // 2
        if A[mid] == x:
            return mid
        elif A[mid] > x:
            return recursive_search(low, mid - 1)
        else:
            return recursive_search(mid + 1, high)
    return recursive_search(0, len(A) - 1)

def test_binary_search():   
    assert binary_search([1,1,2,2,34],34) == 4

class Node:
    def __init__(self, key: Key, val: Value, size: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None
        self.size = size

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def put(self, key: Key, val: Value) -> None:
        if val is None:
            self.delete(key)
            return
        self.root = self._put(self.root, key, val)

    def _put(self, x: Optional[Node], key: Key, val: Value) -> Node:
        if not x:
            return self.Node(key, val, 1)
        if key < x.key:
            x.left = self._put(x.left, key, val)
        elif key > x.key:
            x.right = self._put(x.right, key, val)
        else:
            x.val = val
        x.size = 1 + self._size(x.left) + self._size(x.right)
        return x

    def _delete(self, x: Optional[Node], key: Key) -> Optional[Node]:
        if not x:
            return None
        if key < x.key:
            x.left = self._delete(x.left, key)
        elif key > x.key:
            x.right = self._delete(x.right, key)
        else:
            if not x.right:
                return x.left
            if not x.left:
                return x.right
            t = x
            x = self._min(t.right)
            x.right = self._delete_min(t.right)
            x.left = t.left
        x.size = 1 + self._size(x.left) + self._size(x.right)
        return x    
    
def test_bst():
    bst = BinarySearchTree()
    bst.put("A",1)
    #bst.search(2)
    #bst.add(3)
    #bst.delete(5)

def main():
    test_binary_search()

# O(logn)
# AC Leetcode 501, implementation of binary search tree data structure
if __name__ == '__main__':
    main()