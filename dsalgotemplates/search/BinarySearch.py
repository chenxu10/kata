class BinarySearch():
    """
    Variation when floor return hi, when ceiling return lo
    """
    def __init__(self, sorted_array):
        self.sorted_array = sorted_array

    def indexOf(self, k):
        lo = 0
        hi = len(self.sorted_array) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if k < self.sorted_array[mid]:
                hi = mid - 1
            elif k > self.sorted_array[mid]:
                lo = mid + 1
            else:
                return mid
                
        return -1

    def floor(self,k):
        """
        Find the smallest index equals to k

        [1,2,2,2,3] 2 --> 1
        """
        lo = 0
        hi = len(self.sorted_array) # different from index

        while lo < hi: # break when lo == hi
            mid = lo + (hi - lo) // 2
            if k < self.sorted_array[mid]: #[lo, mid)
                hi = mid
            elif k > self.sorted_array[mid]: #[mid + 1, hi)
                lo = mid + 1
            elif k == self.sorted_array[mid]: # this guarantees the floor return becasue it doesn't return immediately
                hi = mid
                
        return lo

    def ceil(self, k):
        """
        Find the largest index equals to k
        """
        lo = 0
        hi = len(self.sorted_array) # different from index

        while lo < hi: # break when lo == hi
            mid = lo + (hi - lo) // 2
            if k < self.sorted_array[mid]: #[lo, mid)
                hi = mid
            elif k > self.sorted_array[mid]: #[mid + 1, hi)
                lo = mid + 1
            elif k == self.sorted_array[mid]: # this guarantees the floow return becasue it doesn't return immediately
                lo = mid + 1
                
        return lo - 1

def testBinarySearch():
    array = [1,2,2,2,3]
    sorted_array = sorted(array)
    k = 2
    BS = BinarySearch(sorted_array)
    
    index = BS.indexOf(k)
    if index == -1:
        print("No index founded")
    else:
        print(index)

    floorindex = BS.floor(k)
    print(floorindex)

    ceilindex = BS.ceil(k)
    print(ceilindex)

def isOK():
    pass

def binary_search_target_template():
    """
    搜索空间[lo, hi)
    模板的关键在于左右都是闭区间
    [mid + 1, ],
    [lo, mid]
    """
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if isOK(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


if __name__ == '__main__':
    testBinarySearch()