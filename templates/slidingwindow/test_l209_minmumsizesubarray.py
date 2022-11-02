import typing
from typing import List

"""
初始化慢指针 = 0
初始化 ans

for 快指针 in 可迭代集合
   更新窗口内信息
   while 窗口内不符合题意
      扩展或者收缩窗口
      慢指针移动
   更新答案
返回 ans
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = total = 0
        ans = len(nums) + 1
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                ans = min(ans, r - l + 1)
                total -= nums[l]
                l += 1
        
        return 0 if ans == len(nums) + 1 else ans


def non_decreasing(x):
    if len(x) == 1 or len(x) == 0:
        return True
    for i in range(len(x)):
        if x[i] < x[i - 1]:
            return False
    return True

if __name__ == '__main__':
    print(non_decreasing([1,3]))

