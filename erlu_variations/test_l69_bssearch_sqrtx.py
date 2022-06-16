def sqrt(x):
    lo = 1
    hi = x
    
    while lo <= hi:
        mid = lo + (hi - lo) // 2 # 2
        
        if mid ** 2 < x:
            lo = mid + 1 # lo = 2
        elif mid ** 2 > x:
            hi = mid - 1 # hi=3
        else:
            return mid
    
    return hi

def test_sqrt():
    print(sqrt(9))
    print(sqrt(0))
    print(sqrt(1))  
    print(sqrt(8))
    # assert sqrt(9)==3
    # assert sqrt(17)==5

if __name__ == '__main__':
    test_sqrt()