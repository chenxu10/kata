
def knapsack(weights, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weights[i-1]] + weights[i-1])
            else:
                dp[i][w] = dp[i-1][w]
    
    return dp[n][capacity]

def longestCommonSubsequence(s1,s2):
    n = len(s1)
    m = len(s2)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = max(dp[i - 1][j - 1] + (s1[i - 1] == s2[j - 1]), 
                        max(dp[i - 1][j],dp[i][j - 1]))

    return dp[-1][-1]

# Leetcode198
# dp一维数组线性扫描
def houserob(nums):
    n = len(nums)
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, n):      
        dp[i] = max(dp[i-2]+nums[i], dp[i-1])

    return dp[n-1] 

def test_rob():
    assert houserob([]) == 0
    assert houserob([2]) == 2
    assert houserob([1,2,3,1]) == 4
    assert houserob([1,4,1]) == 4