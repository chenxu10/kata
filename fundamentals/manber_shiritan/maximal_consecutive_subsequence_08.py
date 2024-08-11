"""
Application:
How much money you lose most?
How long the worst season will last?
"""

def mcs(x):
    """
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

def longest_consecutive_sequence(x):
    """
    We know how to find in sequences of size < n, the longest subsequence
    and the longest subsequence must begin with that number is the lower bound
    and prefix of that string
    """
    hashset = set(x)
    ans = 0

    # make sure it's lower bound
    for i in x:
        if (i - 1) not in hashset: # lower bound
            l = 0
            while i in hashset:
                l += 1
                i += 1
                ans = max(ans, l)
    return ans


def test_longest_consecutive_sequence():
    print(longest_consecutive_sequence([100,4,1,2,3]))
    #assert longest_consecutive_sequence([100,4,200,1,2,3]) == len([1,2,3,4])    
    #assert longest_consecutive_sequence([0,6,7,2,3,4,5,6,8,1]) == len([0,1,2,3,4,5,6,7,8])

test_longest_consecutive_sequence()