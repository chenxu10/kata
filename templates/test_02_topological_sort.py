# from utils import Graph
# from collections import defaultdict

# class Graph():
#     def __init__(self,vetices):
#         self.graph = defaultdict(list)
#         self.V = vetices
    
#     def add_edge(self, nodeA, nodeB):
#         self.graph[nodeA].append(nodeB)
 
#     def helper(self, v, visited, stack):

#         visited[v] = True
#         for i in self.graph[v]:
#             if visited[i] == False:
#                 self.helper(i, visited, stack)
            
#         stack.append(v)

#     def topologial_sort(self):
#         visited = [False] * self.V
#         stack = []

#         for i in range(self.V):
#             if visited[i] == False:
#                 self.helper(i, visited, stack)
    
#         return stack[::-1]

# def test_topologial_sort():
#     G = Graph(6)
#     G.add_edge(5,2)
#     G.add_edge(2,3)
#     G.add_edge(3,1)
#     G.add_edge(4,1)
#     G.add_edge(5,0)
#     G.add_edge(4,0)
#     res = G.topologial_sort()
#     print(res)
#     expected = [5,4,2,3,1,0]
#     assert res == expected

# Example Problems
"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you 
must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 
you should also have finished course 1. So it is impossible.

Try to solve it in both acyclic ways and topological ways
"""
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)]
        
        for parent, children in prerequisites:
            graph[parent].append(children)
        
        def dfs(i):
            """
            Returns wether it will encounter cycling

            False means this graph is cyclic
            True means this graph is acyclic
            
            -1 denote course hasn't been encountered
            1 denote course has been encountered
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
                
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

