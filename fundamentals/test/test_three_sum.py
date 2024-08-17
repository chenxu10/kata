
def three_sum(nums):
    ans = []

    if len(nums) < 2:
        return []
    
    nums.sort()
    n = len(nums)
    for i in range(len(nums)):
        j = i + 1
        k = n - 1
        while j < k:
            sol = nums[i] + nums[j] + nums[k]
            if sol == 0:
                ans.append([nums[i],nums[j],nums[k]])
                j += 1
            if sol > 0:
                k -= 1
            if sol < 0:
                j += 1
    return ans


def test_three_sum():
    assert three_sum([]) == []
    assert three_sum([1]) == []
    assert three_sum([0,1,1]) == []
    assert three_sum([-1,0,1]) == [[-1,0,1]]
    print(three_sum([-1,0,3,1]))
    assert three_sum([-1,0,3,1]) == [[-1,0,1]]
    assert three_sum([-1,0,3,3,1]) == [[-1,0,1]]

def main():
    test_three_sum()
    
if __name__ == '__main__':
    main()

