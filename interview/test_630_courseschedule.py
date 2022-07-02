from typing import List

"""
There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.

You will start on the 1st day and you cannot take two or more courses simultaneously.

Return the maximum number of courses that you can take.

Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
Output: 3
"""

from heapq import heappush, heappop

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        t = 0
        maxheap = []
        courses.sort(key=lambda x:x[1])
        
        for duration, enddate in courses:
            heappush(maxheap, -duration)
            t += duration
            if t > enddate:
                t += heappop(maxheap)
                
        return len(maxheap)
                
            
        
        



