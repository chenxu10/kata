




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