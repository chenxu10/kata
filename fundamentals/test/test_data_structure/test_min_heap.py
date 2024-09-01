import pytest
from fundamentals.dsalgo.min_heap import MinHeap

def test_create_empty_heap():
    heap = MinHeap()
    assert len(heap) == 0

def test_insert_single_element():
    heap = MinHeap()
    heap.insert(5)
    assert len(heap) == 1
    assert heap.peek() == 5

def test_insert_multiple_elements():
    heap = MinHeap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(7)
    assert len(heap) == 3
    assert heap.peek() == 3

def test_remove_min():
    heap = MinHeap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(7)
    min_value = heap.remove_min()
    assert min_value == 3
    assert len(heap) == 2
    assert heap.peek() == 5

def test_build_heap():
    arr = [5, 3, 7, 1, 4, 6]
    heap = MinHeap.build_heap(arr)
    assert len(heap) == 6
    assert heap.peek() == 1
    assert heap.remove_min() == 1
    assert heap.remove_min() == 3
    assert heap.remove_min() == 4

def test_empty_heap_peek():
    heap = MinHeap()
    assert heap.peek() is None

def test_empty_heap_remove_min():
    heap = MinHeap()
    assert heap.remove_min() is None

def test_heapify_up():
    heap = MinHeap()
    heap.insert(5)
    heap.insert(3)
    heap.insert(7)
    heap.insert(1)
    assert heap.peek() == 1
    assert len(heap) == 4

