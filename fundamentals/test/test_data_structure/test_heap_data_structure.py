from fundamentals.dsalgo.heap import binaryheap as bh

def test_build_heap_data_structure():
    A = [4, 10, 3, 5, 1]
    binaryheap  = bh.BinaryHeap()
    binaryheap.sort(A)
    assert binaryheap.is_sorted(A)
    
if __name__ == "__main__":
    test_build_heap_data_structure()