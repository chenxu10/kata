"""
There are n cities labeled from 1 to n. You are given the integer n and an array connections where connections[i] = [xi, yi, costi] indicates that the cost of connecting city xi and city yi (bidirectional connection) is costi.

Return the minimum cost to connect all the n cities such that there is at least one path between each pair of cities. If it is impossible to connect all the n cities, return -1,

The cost is the sum of the connections' costs used.

Input: n = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6
"""

from collections import defaultdict
from heapq import heappop, heappush
from typing import List

class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        visited = set()
        total_cost = 0
        MST = {}
        mst = {}
        minqueue = [(0,connections[0][0])]
        
        # graph processing default dict
        G = defaultdict(list)
        
        for nodeA, nodeB, cost in connections:
            G[nodeA].append((cost, nodeB))
            G[nodeB].append((cost, nodeA))
            
                
        def visit(node):
            visited.add(node)
            for edge_cost, nei in G[node]:
                if nei not in visited:
                    heappush(minqueue, (edge_cost, nei))
                    MST[n] = (edge_cost, node)
                    mst[node] = (edge_cost, nei)
        
        def prim():
            nonlocal total_cost
            while minqueue and len(visited) < n:
                cost, node = heappop(minqueue)    
                if node not in visited:
                    total_cost += cost
                    visit(node)
                    
        prim()
        if len(visited) == n:
            return total_cost
        else:
            return -1
        