# Cheatsheet
## DP
```python
def dp(nums):
    n = len(nums)
    dp = [[] for _ in range(n + 1)] 
    # The definition of dp should copied from problem's
    #asking, range(should be n+1)
    for i in range(1, n+1): 
    # starting from 1, the first element in nums
        dp[i] = dp[i - 1] + nums[i - 1]
    # should pay attention here the choice of decision should be i - 1
    # aggregation function varies as problem change can be sum, max, min
    result = agg(dp)
```
### Taolu
+ dp[i][j] stands for in the ith round j choices
+ Build connections between (dp[i-1][j] and dp[i])
+ aggregate(dp[last][j])