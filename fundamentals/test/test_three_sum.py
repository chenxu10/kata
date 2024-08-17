






def three_sum(nums):
    ans = []

    if len(nums) < 2:
        return []
    else:
        sol = nums[0] + nums[1] + nums[2]
        if sol == 0:
            ans.append([nums[0],nums[1],nums[2]])
    return ans


def test_three_sum():
    assert three_sum([]) == []
    assert three_sum([1]) == []
    assert three_sum([0,1,1]) == []
    assert three_sum([-1,0,1]) == [[-1,0,1]]

def main():
    test_three_sum()
    
if __name__ == '__main__':
    main()

