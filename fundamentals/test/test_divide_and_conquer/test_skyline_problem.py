from fundamentals.manbercreativemethod import compute_balancing_factor_07 as cb

def test_merge_sort():
    assert cb.merge_sort([1]) == [1]
    assert cb.merge_sort([1,3,6,5]) == [1,3,5,6]

def test_skyline():
    assert cb.getSkyline([[0,2,3],[2,5,3]]) == [5,0]
