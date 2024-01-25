"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""
from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        
        for parent, children in prerequisites:
            graph[parent].append(children)
        
        def dfs(i):
            """
            dfs no circle

            return True if no cycle
            return False if cycle
            """
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            
            visit[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            
            visit[i] = 1
            return True

        # dealing with edge case logic [[1,0],[0,1]]     
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

def canfinish(numsCourses, prerequisites):
    """
    Given a directed graph, can you detect the cirle    
    """
    graph = defaultdict(list)
    for children, parent in prerequisites:
        graph[parent].append(children)

    marked = [None for _ in range(numsCourses)]
    onStack = [None for _ in range(numsCourses)]
    hasCycle = False

    def detect_cyle(graph, node):
        nonlocal hasCycle

        onStack[node] = True
        marked[node] = True
        for w in graph[node]:
            if hasCycle:
                return
            elif not marked[w]:
                detect_cyle(graph, w)
            elif onStack[node]:
                hasCycle = True

        onStack[node] = False

    for i in range(numsCourses):
        detect_cyle(graph, i)

    return not hasCycle

def test_canfinish():
    assert canfinish(2,[[1,0]]) == True
    assert canfinish(2,[[1,0],[0,1]]) == False
    assert canfinish(20,[[0,10],[3,18],[5,5],[6,11],[11,14],[13,1],[15,1],[17,4]]) == False

if __name__ == '__main__':
    test_canfinish()