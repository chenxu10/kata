def h_index(citations):
    hindex = 0
 
    # Set the range for binary search
    low = 0
    high = len(citations) - 1
 
    while (low <= high):
        mid = (low + high) // 2
 
        # Check if current citations is
        # possible
        if (citations[mid] >= (mid + 1)):
            # Check to the right of mid
            low = mid + 1
            # Update h-index
            hindex = mid + 1
 
        else:     
            # Since current value is not
            # possible, check to the left
            # of mid
            high = mid - 1
 
    # Print the h-index
    print(hindex)
    return hindex

def test_h_index():
    assert h_index([]) == 0
    assert h_index([4,0,6,1,5])==3