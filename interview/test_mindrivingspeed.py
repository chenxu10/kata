
# P([], 8) --> min()
from math import ceil
# Normal Solution
# Calculate hour for each binary search trial
def calculate_hour(arr, speed):
    hourtaken = 0
    for i in arr:
        hourtaken += i / speed
        if i % speed != 0:
            hourtaken += 1
    return hourtaken

# Optimial Solution
def drivingspeed(piles, H):
    """
    using binary search left to find the left smallest
    """
    beg, end = 1, max(piles)
    while beg < end:
        mid = beg + (end - beg) // 2
        print(mid)
        if sum(ceil(i/mid) for i in piles) > H:
            beg = mid + 1
        else:
            end = mid
            
    return beg

def test_mindrivingspeed():
    assert drivingspeed([10],5) == 2
    assert drivingspeed([3,4,7],5) == 4
    assert drivingspeed([3,6,7,11],8) == 4

# Failed at didn't come up with binary search natutally
# Learnt lessons: XXXX
# Lee binary search explanation
# Should be realted to question leetcode 875
# Related Problems

# Leetcode410: 
# Iterate through all inserting indexes and calculate the sum, update the maximum
# if necessary
# Leetcode774:
# Leetcode1011:
# Capacity to ship packages in N days
# Leetcode875:Koto eating bananas
# Leetcode1231:Divide chocolate(recursively doinb BS search)