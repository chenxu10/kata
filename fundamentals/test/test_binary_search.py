

def binary_search(arr,start,end,k):
    arr.sort()
    
    if len(arr) == 0:
        return
    mid = (start + end) // 2
    if arr[mid] == k:
        return mid
    if arr[mid] > k:
        binary_search(arr, start, mid - 1, k)
    else:
        binary_search(arr, mid + 1, end, k)

def test_binary_search():
    assert binary_search([2,34,2,1,1],0,5,34) == 1


def main():
    test_binary_search()
if __name__ == '__main__':
    main()