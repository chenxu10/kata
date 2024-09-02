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

def test_maxUniqueSubarraySum():
    nums = [5, 3, 5, 1, 4, 8, 9]
    assert maxUniqueSubarraySum(nums) == 30

if __name__ == "__main__":
    test_maxUniqueSubarraySum()