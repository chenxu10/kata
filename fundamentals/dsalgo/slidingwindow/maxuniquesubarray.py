"""
Sliding Window Techniques are
- Good at finding substring pattern matching problem
- Optimize from multiple pass to one pass
- Can be replaced by dynamic programming
"""

def maxUniqueSubarraySum(nums):
    left = 0 
    max_sum = 0
    cur_sum = 0
    unique_set = set()

    for right in range(len(nums)):
        while nums[right] in unique_set:
            unique_set.remove(nums[left])
            cur_sum -= nums[left]
            left += 1
        
        unique_set.add(nums[right])
        cur_sum += nums[right]
        max_sum = max(max_sum, cur_sum)

    return max_sum