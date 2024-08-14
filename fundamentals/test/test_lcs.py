import pytest

from fundamentals.manbercreativemethod.knapsack_10 import longestCommonSubsequence

# Related Problems
# Leetcodel718
@pytest.mark.parametrize(
    "s1,s2,expected",
    [("abcde","ace",3)])
def test_lcs(s1,s2,expected):
    assert expected == longestCommonSubsequence(s1,s2)

