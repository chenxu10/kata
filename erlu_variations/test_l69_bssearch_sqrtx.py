def sqrt(x):
    if x < 2:
        return x
    start = 1
    end = x
    
    while start <= end:
        mid = start + (end - start) // 2
        if mid ** 2 == x:
            return mid
        elif mid ** 2 < x:
            start = mid + 1
        else:
            end = mid - 1
    
    return start

def test_sqrt():
    assert sqrt(9)==3
    assert sqrt(17)==5