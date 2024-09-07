from fundamentals.manbercreativemethod.maximal_consecutive_subsequence_08 import maximum_subarray, maximum_subarray_divide_conquer

def calculate_cross_sum(nums, low, high):
    mid = (low + high) // 2
    left_sum = float('-inf')
    right_sum = float('-inf')
    current_sum = 0

    # Calculate left sum
    for i in range(mid, low - 1, -1):
        current_sum += nums[i]
        left_sum = max(left_sum, current_sum)

    current_sum = 0

    # Calculate right sum
    for i in range(mid + 1, high + 1):
        current_sum += nums[i]
        right_sum = max(right_sum, current_sum)

    return left_sum + right_sum

def test_largest_interval_series():
    assert maximum_subarray([2,-1,5])==6
    assert maximum_subarray([2,5,-5,10,15,20,-5])==47
    assert maximum_subarray([5,4,-1,7,8]) == 23
    assert maximum_subarray([1]) == 1
    assert maximum_subarray([-1,-2]) == -1
    assert maximum_subarray_divide_conquer([2,-1,5])==6
    assert maximum_subarray_divide_conquer([2,5,-5,10,15,20,-5])==47
    #print(maximum_subarray_divide_conquer([23.2,3.2,-1.4,-12.2,34.2,5.4]))



def test_calculate_cross_sum():
    assert calculate_cross_sum([-1,2,3,-1], 0, 3) == 5

def main():
    test_largest_interval_series()
    test_calculate_cross_sum()
    

if __name__ == '__main__':
    main()