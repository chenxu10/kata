"""
You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.
Return the intersection of these two interval lists.
A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.
The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].
"""
from typing import List

class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0

        ans = []
        while (i < len(A) and j < len(B)):
            s = max(A[i][0], B[j][0])
            print("s",s)
            e = min(A[i][1], B[j][1])
            print("e",e)
            if s <= e:
                ans.append([s,e])
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return ans

"""
Tricks:
(1)If interval problem, compare previous max and before minimum and think of two pointers
(2)Trading with other programmers is a lot of fun, do it yourself first and observe what they do
"""