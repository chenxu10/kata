from fundamentals.manbercreativemethod.compute_balancing_factor_07 import merge_sort_memory_improve

def test_merge_sort(arr):
    """
    """
    arr = [2,3,4,1,-1]
    print(merge_sort_memory_improve(arr))
    assert(merge_sort_memory_improve(arr,0,len(arr)-1)==[-1,1,2,3,4])


