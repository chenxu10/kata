"""
Given a list of non-negative integers nums, 
arrange them such that they form the largest number and return it.
Since the result may be very large, so you need to return a string instead of an integer.


Input: nums = [10,2]
Output: "210"

Input: nums = [3,30,34,5,9]
Output: "9534330"
"""

# sorting + greedy




def largestnumber(nums):
    nums = [str(i) for i in nums]
    nums = sorted(nums, key=lambda x: int(x[0]), reverse=True)
    ans = "".join(nums)
    return ans

