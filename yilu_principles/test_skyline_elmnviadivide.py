# Mimic the thoughts of merge thought
def mergeskyline(left, right):
    """
    Mimic the logic of merge sort
    """
    n_l = len(left)
    n_r = len(right)
    p_l = p_r = 0 
    curr_y = curr_l = curr_r = 0

    while p_l < n_l and p_r < n_r:
        point_l = left[p_l]
        point_r = right[p_r]
        if point_l[0] < point_r:
            x, left_y = point_l
            p_l += 1
        else:
            x, right_y = point_r
            p_r += 1
        max_y = max(left_y, right_y)

        if cur_y != max_y:
            cur_y = max_y

def skyline(input):
    n = len(input)
    if not input:
        return []
    if len(input) == 1:
        ans = []
        ans.append([input[0][0],input[0][2]])
        ans.append([input[0][1],input[0][0]])   
    leftskyline = skyline(input[:n//2])
    rightskyline= skyline(input[n//2:])
    ans = mergeskyline(leftskyline,rightskyline)
    # merge those together
    return ans       

def test_skyline():
    assert mergeskyline([
        [0,3],
        [5,0]])
    
    assert skyline([[0,2,3]])==[[0,3],[2,0]]
    assert skyline([[0,2,3],[2,5,3]])==[[0,3],[5,0]]
    # assert skyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]) == [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
    # assert skyline([(1,11,5),(2,6,7),(3,13,9),(12,7,16)]) == [(1,11),(3,13),(9,0),(12,7)]

# Related leetcode 218