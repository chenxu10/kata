def countSubarrays(nums, minK, maxK):
    
    res = 0
    for i in enumerate(nums):
        if i[1] >= minK and i[1] <= maxK:
            res += 1
            for j in enumerate(nums[i[0]+1:]):
                if j[1] >= minK and j[1] <= maxK:
                    res += 1
                else:
                    break
    return res
    
