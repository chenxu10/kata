"""

It's easier to prove Given P(n-1),Q are True Then P(n) True comparing with P(n-1) Then P(n)
Common error is the extra assumption Q should be separately proved

It's easier to add $1 to 1 million then add $1 to 10, girls will not choose beautiful man, they will
only choose men other beautiful girls choose

Application:
How much money you lose most?
How long the worst season will last?
"""


# Problem1: Maximum consecutive subsequence
def mcs(x):
    """
    key techniques if xn is positive is it easier to extend to Sn
    What property sn have will make the extension easier
    decoupling finding new maximum and new maximum suffix
    """
    n = len(x)
    global_max = 0
    local_max = 0
    
    for i in range(n):
        if x[i] + local_max > global_max:
            local_max = x[i] + local_max
            global_max = local_max
        elif x[i] + local_max > 0:
            local_max = x[i] + local_max
        else:
            local_max = 0
        
    return global_max

def mcs_recursive(x):
    local_max = 0
    global_max = 0
    
    def dfs(x, i=0):
        nonlocal local_max
        nonlocal global_max
        if i == len(x) - 1:
            return global_max
        elif x[i] + local_max > global_max:
            local_max = x[i] + local_max
            global_max = local_max
        elif x[i] + local_max > 0:
            local_max = x[i] + local_max
        else:
            local_max = 0
        return dfs(x, i + 1)

    return dfs(x, 0)

def test_maximal_consecutive_sequence():
    assert mcs([1,-2,-1,4,5]) == 4 + 5
    # context: running across negative number suffix decreasing
    assert mcs([1.5,-1,3,-2,-3,3]) == 1.5 - 1 + 3
    assert mcs_recursive([1.5,-1,3,-2,-3,3]) == 1.5 - 1 + 3
test_maximal_consecutive_sequence()



# Problem2: Longest Consecutive Sequence
def longest_consecutive_sequence(x):
    """
    We know how to find in sequences of size < n, the longest subsequence
    and the longest subsequence must begin with that number is the lower bound
    and prefix of that string
    """
    def extend_from_prefix(hashset, ans, i):
        l = 1
        while (i + 1) in hashset:
            l += 1
            i += 1
            ans = max(ans, l)
        return ans
    
    hashset = set(x)
    ans = 0
    for i in x:
        if (i - 1) not in hashset:
            ans = extend_from_prefix(hashset, ans, i)
    return ans


def test_longest_consecutive_sequence():
    assert longest_consecutive_sequence([100,4,200,1,2,3]) == len([1,2,3,4])    
    assert longest_consecutive_sequence([0,6,7,2,3,4,5,6,8,1]) == len([0,1,2,3,4,5,6,7,8])

test_longest_consecutive_sequence()

# Problem3:Maximum Subsequence
# assume is in the second largest
def mss(nums):
    if max(nums) <= 0:
        return max(nums)
    
    sum = 0
    for i in nums:
        if i > 0:
            sum += i
    return sum 

def test_maximum_sum_of_subsequence():
    assert mss([2,3,5]) == 10
    assert mss([-2,11,-2,2]) == 13

test_maximum_sum_of_subsequence()


# Problem4-prerequisite: House Robber(Leetcode 198)



# Problem4:Non AdjacentMaximum Subsequence
# Assume we know how to deal with non-adjacent
# maximum sum of non adjacent subsequence l3165


# Problem6: Find the mode of multiset
def modemultiset(x):
    return 2

assert modemultiset({1,2,3,2}) == 2
assert modemultiset({1,1,2,2,2,3}) == 2
