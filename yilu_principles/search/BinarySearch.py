class BinarySearch():
    """
    Variation when floor return hi, when ceiling return lo
    """
    def indexOf(self, sorted_array, k):
        lo = 0
        hi = len(sorted_array) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if k < sorted_array[mid]:
                hi = mid - 1
            elif k > sorted_array[mid]:
                lo = mid + 1
            else:
                return mid
                
        return -1

def testBinarySearch():
    array = [-1,0,9,-2,4]
    sorted_array = sorted(array)
    k = 4
    BS = BinarySearch()
    
    index = BS.indexOf(sorted_array, k)
    if index == -1:
        print("No index founded")
    else:
        print(index)

if __name__ == '__main__':
    testBinarySearch()