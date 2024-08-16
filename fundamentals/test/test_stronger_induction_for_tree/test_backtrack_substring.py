from fundamentals.manbercreativemethod import compute_balancing_factor_07 as cb
# Leetcode 2767

def test_backtrack_substring():
    s = "1011"
    output = 2
    print(cb.backtrack_substring(s))
    assert cb.backtrack_substring(s) == output