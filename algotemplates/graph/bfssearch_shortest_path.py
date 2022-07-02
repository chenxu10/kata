from collections import defaultdict, OrderedDict, deque

class BreadthFirstSearch():
    inf = float("inf")

    def __init__(self, G, sources):
        self.marked = OrderedDict([(vertex, False) for vertex in G])
        self.edge_to = OrderedDict([(vertex, self.inf) for vertex in G])
        self.dist_to = OrderedDict([(vertex, self.inf) for vertex in G])
        self._bfs(G, sources)

    def deque(self, queue):
        vertex = queue.popleft()
        return vertex

    def _bfs(self, G, sources):
        """
        Takes in a graph and single source
        starting visit new node in a bfs way
        mark them and add them to distto
        the algorithm is implemented iteratively
        """
        queue = deque()

        for s in sources:
            self.marked[s] = True
            self.edge_to[s] = s
            self.dist_to[s] = 0
            queue.append(s)

        while queue:
            vertex = self.deque(queue)
            for w in G[vertex]:
                if not self.marked[w]:
                    self.marked[w] = True
                    self.edge_to[w] = vertex
                    self.dist_to[w] = self.dist_to[vertex] + 1
                    queue.append(w)
        return

    def hasPathTo(self, v):
        return self.marked[v]

    def PathTo(self, v):
        """
        Returns the shortest path from source or sources
        to node V
        """
        if not self.hasPathTo(v):
            return 
        
        path = []
        x = v

        while self.dist_to[x] != 0:
            path.append(x)
            x = self.edge_to[x]
        path.append(x) 
        
        return path

def test_bfssearch():
    G = defaultdict(list)
    G[1].append(2)          
    G[1].append(5)
    G[1].append(4)
    G[2].append(1)
    G[2].append(5)
    G[2].append(3)
    G[3].append(4)
    G[3].append(2)
    G[4].append(3)
    G[4].append(1)
    G[5].append(1)
    G[5].append(2)


    bfs = BreadthFirstSearch(G, [1])

    for node in G:
        if bfs.hasPathTo(node):
            print(bfs.PathTo(node))
        else:
            print("This node {} is not reachable from source node".format(node))


if __name__ == '__main__':
    test_bfssearch()