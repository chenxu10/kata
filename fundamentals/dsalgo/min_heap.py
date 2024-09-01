class MinHeap:
    def __init__(self):
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def peek(self):
        if not self.heap:
            return None
        return self.heap[0]

    def _heapify_up(self, index):
        parent = (index - 1) // 2
        if index > 0 and self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            self._heapify_up(parent)

    def remove_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return min_value

    def _heapify_down(self, index):
        min_index = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left
        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right

        if min_index != index:
            self.heap[index], self.heap[min_index] = self.heap[min_index], self.heap[index]
            self._heapify_down(min_index)

    @classmethod
    def build_heap(cls, arr):
        heap = cls()
        heap.heap = arr[:]
        for i in range(len(arr) // 2 - 1, -1, -1):
            heap._heapify_down(i)
        return heap