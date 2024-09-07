from fundamentals.manbercreativemethod.maximal_consecutive_subsequence_08 import maximum_subarray, maximum_subarray_divide_conquer

def test_largest_interval_series():
    assert maximum_subarray([2,-1,5])==6
    assert maximum_subarray([2,5,-5,10,15,20,-5])==47
    assert maximum_subarray([5,4,-1,7,8]) == 23
    assert maximum_subarray([1]) == 1
    assert maximum_subarray([-1,-2]) == -1
    assert maximum_subarray_divide_conquer([2,-1,5])==6
    assert maximum_subarray_divide_conquer([2,5,-5,10,15,20,-5])==47
    #print(maximum_subarray_divide_conquer([23.2,3.2,-1.4,-12.2,34.2,5.4]))

def calculate_cross_sum(nums, low, mid, high):
    left_sum = float('-inf')
    local_sum = 0

    for i in range(mid, low - 1, -1):
        local_sum += nums[i]
        left_sum = max(left_sum, local_sum)

    right_sum = float('-inf')
    local_sum = 0

    for j in range(mid + 1, high + 1):
        local_sum += nums[j]
        right_sum = max(right_sum, local_sum)

    return left_sum + right_sum



def test_calculate_cross_sum():
    assert calculate_cross_sum([-1,2,3,-1]) == 5

def main():
    test_largest_interval_series()
    

if __name__ == '__main__':
    main()