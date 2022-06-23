# Motivation(hand writing recognition)
# nuclei in cancer cells
# related to shortest path tree
    # global
    # shortest path tree: local
from heapq import heappush, heappop
from collections import defaultdict

class PrimMST():
    """
    Spanning tree cut propery and contradictory proof
    BFS + heapq
    """
    def __init__(self, G, n, edges):
        self._marked = set()
        self._pq = [(0, edges[0][0])] #Randomly pick a starting node in Binary Heap
        self.total_cost = 0
        self.MST = {} #resulting MST
        self.mst = {} # growing mst
        self.prim(G, n)

    def prim(self, G, n):
        while self._pq and len(self._marked) < n:
            cost, node = heappop(self._pq)

            if node not in self._marked:
                self.total_cost += cost
                self._marked.add(node)

                for edge_cost, nei in G[node]:
                    heappush(self._pq, (edge_cost, nei))
                    self.MST[nei] = (edge_cost, node) # building undirected sub-graph MST
                    self.mst[node] = (edge_cost, nei)

        if len(self._marked) == n:
            return self.total_cost, self.MST

def testMinimumSpinngTree():
    # GraphProcessing
    n = 3
    connections = [[1,2,3],[3,4,4]]
    connections = [[1,2,5],[1,3,6],[2,3,1],[2,4,1]]
    G = defaultdict(list)
    for city1, city2, cost in connections:
        G[city1].append((cost, city2))
        G[city2].append((cost, city1))

    MST = PrimMST(G,n,connections)
    print(MST.prim(G,3))
    
    # {1: [(5, 2), (6, 3)], 2: [(5, 1), (1, 3)], 3: [(6, 1), (1, 2)]})

if __name__ == '__main__':
    testMinimumSpinngTree()
# Application leetcode1135

