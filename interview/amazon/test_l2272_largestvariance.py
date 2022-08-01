def translate_nums(s):
    count = [0] * 26
    for x in s:
        count[ord(x) - ord('a')] += 1   
    translated_arrays = []
    
    for i in range(26):
        for j in range(26):
            if i == j:
                continue
            if (count[i] == 0 or count[j] == 0):
                continue
            nums = [0] * len(s)
            for k in range(len(s)):
                if s[k] == chr(ord('a') + i):
                    nums[k] = 1
                elif s[k] == chr(ord('a') + j):
                    nums[k] = -1
                translated_arrays.append(nums)
    
    return translated_arrays

def maximum_subarray(nums):
    n = len(nums)
    dp = [0 for _ in range(len(nums))]

    cursum = 0
    for i in range(0, n):
        cursum = max(cursum + nums[i], nums[i])
        dp[i] = cursum

    res = 0
    cursum = 0
    for j in range(n - 1, -1, -1):
        cursum = max(cursum + nums[j], nums[j])
        if nums[j] == -1:
            res = max(res, cursum + dp[j] - nums[j])
    return res

def largestVariance(s):
    sol = 0
    subarrays = translate_nums(s)
    print(subarrays)
    for array in subarrays:
        sol = max(sol, maximum_subarray(array))
    return sol

def test_maximum_subarray():
    actual = maximum_subarray([1,-1,1,0,1])
    expected = 2
    actual2 = maximum_subarray([1,-1,1,0,-1])
    expected2 = 1
    assert actual == expected
    assert actual2 == expected2

def test_translate_nums():
    actutalnums = translate_nums("ab")
    expected = [[1, -1], [1, -1], [-1, 1], [-1, 1]]
    assert actutalnums == expected

def test_largestVariance():
    assert largestVariance("aababbb") == 3
    assert largestVariance("abcde") == 0
    assert largestVariance("aabacdbbb") == 3

if __name__ == '__main__':
    # print(test_translate_nums())
    largestVariance("ab")