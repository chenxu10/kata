

def binary_search(arr,start,end,k):
    arr.sort()
    
    if start > end:
        return -1
    mid = (start + end) // 2
    if arr[mid] == k:
        return mid
    if arr[mid] > k:
        return binary_search(arr, start, mid - 1, k)
    else:
        return binary_search(arr, mid + 1, end, k)

def test_binary_search():   
    assert binary_search([1,1,2,2,34],0,4,34) == 4

def main():
    test_binary_search()
if __name__ == '__main__':
    main()