class BinaryHeap:
    
    @classmethod    
    def sink(cls, arr, start_index, length_of_array):
        # Change to the larger of the children's node until all children's node 
        # is smaller than the node
        while 2 * start_index + 1 <= length_of_array:
            j = 2 * start_index + 1
            # larger of the children's node
            if (j < length_of_array) and arr[j] < arr[j + 1]:
                j += 1
            if arr[start_index] > arr[j]:
                break
            arr[start_index], arr[j] = arr[j], arr[start_index]
            start_index = j
        
    @classmethod
    def sort(cls, arr):
        N = len(arr)
        
        # Step 1: Build the heap
        for k in range(N//2, -1, -1):
            cls.sink(arr, k, N - 1)
        
        # Step 2: Sort the array
        for i in range(N - 1, 0, -1):
            # Swap the root (largest element) with the last element
            arr[0], arr[i] = arr[i], arr[0]
            # Restore the heap property for the reduced heap
            cls.sink(arr, 0, i - 1)
        
        return arr
    
    @classmethod
    def is_sorted(cls, arr):
        return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

def test_build_heap_data_structure():
    A = [4, 10, 3, 5, 1]
    bh  = BinaryHeap()
    bh.sort(A)
    assert bh.is_sorted(A)
    
if __name__ == "__main__":
    test_build_heap_data_structure()