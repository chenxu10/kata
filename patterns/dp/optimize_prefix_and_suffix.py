"""
You are given a 0-indexed integer array nums of size n and a positive integer k.

We call an index i in the range k <= i < n - k good if the following conditions are satisfied:

The k elements that are just before the index i are in non-increasing order.
The k elements that are just after the index i are in non-decreasing order.
Return an array of all good indices sorted in increasing order.
"""

class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        ans = []
        n = len(nums)
        dp1, dp2 = [1] * (n + 1), [1] * (n + 1)
        
        for i in range(n):
            if nums[i] <= nums[i - 1]:
                dp1[i] = dp1[i - 1] + 1
            
        for i in range(n-2, -1, -1):
            if nums[i] <= nums[i + 1]:
                dp2[i] = dp2[i + 1] + 1
        
        for i in range(k, n -k):
            if dp1[i - 1]  >= k and dp2[i + 1] >= k:
                ans.append(i)
                
        return ans

# 1. Trapping Rain Water
# 2. Range Sum Query - Immutable
# 3. Running Sum of 2D Array

