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

    A stock zuida zengzhang youxiaoqi
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

def maximum_sum_subsequence(nums,query):
    """
    divide and conquer
    [i x x x k][k + 1 x x x j]
    1        0 0        1

    dp00[i][j] = dp00[i][k] + dp00[k+1][j]
    dp00[i][j] = dp00[i][k] + dp10[k+1][j]
    dp00[i][j] = dp01[i][k] + dp00[k+1][j]
    """
    class SegTreeNode:
        def update_four_divide_status(self):
            self.info11 = max(self.left.info10 + self.right.info01,
                            self.left.info11 + self.right.info01,
                            self.left.info10 + self.right.info11)
            self.info00 = max(self.left.info00 + self.right.info00,
                            self.left.info01 + self.right.info00,
                            self.left.info00 + self.right.info10)
            self.info10 = max(self.left.info10 + self.right.info00,
                            self.left.info10 + self.right.info10,
                            self.left.info11 + self.right.info00)
            self.info01 = max(self.left.info00 + self.right.info01,
                            self.left.info01 + self.right.info01,
                            self.left.info00 + self.right.info11)
        
        def build_mid_left_and_right_subtree(self, a, b, vals):
            mid = (a + b) // 2
            self.left = SegTreeNode(a, mid, vals)
            self.right = SegTreeNode(mid + 1, b, vals)
        
        def __init__(self, a, b, vals):
            self.left = None
            self.right = None
            self.start = a
            self.end = b
            self.info00 = 0
            self.info11 = 0
            self.info01 = -float('inf')
            self.info10 = -float('inf')
            
            if a == b:
                self.info11 = vals[self.start]
                return
            
            self.build_mid_left_and_right_subtree(a, b, vals)           
            self.update_four_divide_status()

        def update_range(self, a, val):
            if a < self.start or a > self.end:
                return
            
            if self.start == self.end:
                self.info00 = 0
                self.info11 = val
                return
            
            self.left.update_range(a, val)
            self.right.update_range(a, val)
            self.update_four_divide_status()

    root = SegTreeNode(0, len(nums) - 1, nums)
    res = 0
    M = 10 ** 9 + 7

    for q in query:
        root.update_range(q[0], q[1])
        res += max(root.info00, root.info01, root.info11, root.info10)
        res % M

    return res



def maximum_subarray(nums):
    ans = float('-inf')

    for i in range(len(nums)):
        local_sum = 0
        for j in range(i, len(nums)):
            local_sum += nums[j]
            ans = max(ans, local_sum)

    return ans

# O(n^3)
# O(n^2)

def maximum_subarray_improve(nums):
    if not nums:
        return 0
    n = len(nums)
    global_max = float('-inf')

    for i in range(n):
        local_sum = 0
        for j in range(i,n):
            local_sum += nums[j]
            global_max = max(global_max, local_sum)
    return global_max

# [x x x x] [x x] [x x]

def maximum_subarray_divide_conquer(nums):
    def calculate_cross_sum(nums, low, mid, high):
        left_sum = float('-inf')
        local_sum = 0

        for i in range(mid, low - 1, -1):
            local_sum += nums[i]
            left_sum = max(left_sum, local_sum)

        right_sum = float('-inf')
        local_sum = 0

        for j in range(mid + 1, high + 1):
            local_sum += nums[j]
            right_sum = max(right_sum, local_sum)

        return left_sum + right_sum
    
    def max_subarray_recursive(nums, low, high):
        if low == high: 
            return nums[low]
        mid = (low + high) // 2
        left_max_subarray = max_subarray_recursive(nums,low,mid)
        right_max_subarray = max_subarray_recursive(nums, mid + 1, high)
        cross_sum = calculate_cross_sum(nums, low, mid, high)
        return max(left_max_subarray, right_max_subarray, cross_sum)
    return max_subarray_recursive(nums, 0, len(nums) - 1)


# def maximum_subarray_divide_conquer(nums):
#     def max_cross_sum(nums, low, mid, high):
#         left_sum = float('-inf')
#         local_sum = 0
#         for i in range(mid, low - 1, -1):
#             local_sum += nums[i]
#             left_sum = max(left_sum, local_sum)

#         right_sum = float('-inf')
#         local_sum = 0
#         for i in range(mid + 1, high + 1):
#             local_sum += nums[i]
#             right_sum = max(right_sum, local_sum)

#         return left_sum + right_sum
    
#     def max_subarray_recursive(nums, low, high):
#         if low == high:
#             return nums[low]
        
#         mid = (low + high) // 2
#         left_sum = max_subarray_recursive(nums, low, mid)
#         right_sum = max_subarray_recursive(nums, mid + 1, high)
#         cross_sum = max_cross_sum(nums, low, mid, high)
#         return max(left_sum, right_sum, cross_sum)
    
#     if not nums:
#         return 0
    
#     return max_subarray_recursive(nums, 0, len(nums) - 1)


def maximum_subarray_dp(nums):
    res = nums[0]
    dp = [None for _ in range(len(nums))]
    dp[0] = nums[0]

    for i in range(1, len(nums)):
        dp[i] = max(dp[i-1] + nums[i], nums[i])
        res = max(res, dp[i])

    return res

# Challenge solve it with zero space complexity and use double pointers



