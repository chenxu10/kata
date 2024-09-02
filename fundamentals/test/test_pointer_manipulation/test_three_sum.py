
def three_sum(nums):
    nums.sort()
    n = len(nums)
    res = []
    
    for i in range(n):
        if i == 0 or (nums[i - 1] != nums[i]):
            j = i + 1
            k = n - 1
        while j < k:
            ans = nums[i] + nums[j] + nums[k]
            if ans == 0:
                res.append([nums[i], nums[j], nums[k]])
                j += 1
                while j < k and nums[j - 1] == nums[j]:
                    j += 1
            if ans > 0:
                k -= 1
            if ans < 0:
                j += 1

    return res

def test_three_sum():
    assert three_sum([]) == []
    assert three_sum([1]) == []
    assert three_sum([0,1,1]) == []
    assert three_sum([-1,0,1]) == [[-1,0,1]]
    assert three_sum([-1,0,3,1]) == [[-1,0,1]]
    assert three_sum([-1,0,3,3,1]) == [[-1,0,1]]
    assert three_sum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
def main():
    test_three_sum()
    
if __name__ == '__main__':
    main()

