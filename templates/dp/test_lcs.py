import pytest

def longestCommonSubsequence(s1,s2):
    n = len(s1)
    m = len(s2)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = max(dp[i - 1][j - 1] + (s1[i - 1] == s2[j - 1]), 
                        max(dp[i - 1][j],dp[i][j - 1]))

    return dp[-1][-1]

@pytest.mark.parametrize(
    "s1,s2,expected",
    [("abcde","ace",3)])
def test_lcs(s1,s2,expected):
    assert expected == longestCommonSubsequence(s1,s2)

# Related Problems
# Leetcodel718
