"""
Given a non-empty array nums containing only positive integers, 
find if the array can be partitioned into two subsets such that 
the sum of elements in both subsets is equal.
"""

def can_partition(nums):
    sumnums = sum(nums)
    if sumnums % 2 != 0:
        return False
    
    # transfer this problem into 0-1 knapsack problem
    sumnums = sumnums // 2
    n = len(nums)
    dp = [[False for _ in range(sumnums+1)] for _ in range(n+1)]

    # base case
    dp[0][0] = True

    for i in range(1, n + 1):
        dp[i][0] = True

    for j in range(1, sumnums + 1):
        dp[0][j] = False

    for i in range(1, n + 1):
        for j in range(1, sumnums + 1):
            if nums[i-1] > j: # 包重量不够
                dp[i][j] = dp[i-1][j]
            else: #装入或者不装入
                dp[i][j] = (dp[i][j] or dp[i - 1][j - nums[i - 1]])

    return dp[n][sumnums]

def test_canparition():
    input = [1,5,5,11]
    expected = True
    assert can_partition(input) == expected
