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