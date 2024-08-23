from fundamentals.manbercreativemethod.maximal_consecutive_subsequence_08 import maximum_subarray, maximum_subarray_divide_conquer

def test_largest_interval_series():
    # assert maximum_subarray([2,-1,5])==6
    # assert maximum_subarray([2,5,-5,10,15,20,-5])==47
    # assert maximum_subarray([5,4,-1,7,8]) == 23
    # assert maximum_subarray([1]) == 1
    print(maximum_subarray([-1,-2])) == -1
    #assert maximum_subarray_divide_conquer([2,-1,5])==6
    #assert maximum_subarray_divide_conquer([2,5,-5,10,15,20,-5])==47
    #print(maximum_subarray_divide_conquer([23.2,3.2,-1.4,-12.2,34.2,5.4]))

def main():
    test_largest_interval_series()

if __name__ == '__main__':
    print(23.2+3.2-1.4-12.2+34.2+5.4)
    main()