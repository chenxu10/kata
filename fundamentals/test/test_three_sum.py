
def three_sum(nums):
    ans = []

    if len(nums) < 2:
        return []
    
    nums.sort()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                sol = nums[i] + nums[j] + nums[k]
                if sol == 0:
                    ans.append([nums[i],nums[j],nums[k]])
    return ans


def test_three_sum():
    assert three_sum([]) == []
    assert three_sum([1]) == []
    assert three_sum([0,1,1]) == []
    assert three_sum([-1,0,1]) == [[-1,0,1]]
    assert three_sum([-1,0,3,1]) == [[-1,0,1]]
    assert three_sum([-1,0,3,3,1]) == [[-1,0,1]]

def main():
    test_three_sum()
    
if __name__ == '__main__':
    main()

