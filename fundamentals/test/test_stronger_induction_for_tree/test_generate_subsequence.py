from fundamentals.manbercreativemethod.compute_balancing_factor_07 import generate_subsequence

def test_generate_subsequence():
    print(generate_subsequence([1,2]))
    assert generate_subsequence([1,2]) == [[1,2],[1],[2],[]]