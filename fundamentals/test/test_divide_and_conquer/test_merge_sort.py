from fundamentals.manbercreativemethod.compute_balancing_factor_07 import merge_sort_memory_improve

def test_merge_sort():
    """
    """
    arr = [2,3,4,1,-1]
    assert(merge_sort_memory_improve(arr,0,len(arr)-1)==[-1,1,2,3,4])


def main():
    test_merge_sort()
if __name__ == '__main__':
    main()