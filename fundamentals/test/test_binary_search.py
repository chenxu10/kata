

def binary_search(A,x):
    def recursive_search(low, high):
        if low > high:
            return -1  # x is not in the array
        
        mid = (low + high) // 2
        
        if A[mid] == x:
            return mid  # x found at index mid
        elif A[mid] > x:
            return recursive_search(low, mid - 1)  # search in the left subarray
        else:
            return recursive_search(mid + 1, high)  # search in the right subarray

    return recursive_search(0, len(A) - 1)

def test_binary_search():   
    assert binary_search([1,1,2,2,34],34) == 4

def main():
    test_binary_search()
if __name__ == '__main__':
    main()