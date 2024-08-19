

def binary_search(A,x):
    def recursive_search(low,high):
        if low > high:
            return -1
        mid = (low + high) // 2        
        if A[mid] == x:
            return mid
        if A[mid] > x:
            return recursive_search(low, mid -1)
        if A[mid] < x:
            return recursive_search(mid + 1, high)
    return recursive_search(0, len(A) - 1)

def test_binary_search():   
    assert binary_search([1,1,2,2,34],34) == 4

def main():
    test_binary_search()

# O(logn)
if __name__ == '__main__':
    main()