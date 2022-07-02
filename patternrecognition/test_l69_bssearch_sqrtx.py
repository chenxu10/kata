def sqrt(x):
    """
    sqrt(9) == 3
    sqrt(17) == 4
    
    Ceil integer of binary search
    """
    lo = 1
    hi = x

    while lo <= hi: #[lo, hi]
        mid = lo + (hi - lo) // 2
        if x < mid ** 2:
            hi = mid - 1 # [lo, mid - 1]
        elif x > mid ** 2:
            lo = mid + 1 
        else:
            return mid
    return hi

def test_sqrt():
    assert sqrt(9)==3
    assert sqrt(17)==4
    assert sqrt(26)==5

if __name__ == '__main__':
    test_sqrt()