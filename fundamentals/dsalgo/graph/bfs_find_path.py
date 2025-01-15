from collections import defaultdict
from queue import deque

class BFS:
    def __init__(self,G,s) -> None:
        self.G = G
        self.s = s
        self.edge_to = defaultdict()
        self.visited = set()
        self._bfs_traverse()

    def _bfs_traverse(self):
        q = deque([self.s])
        while q:
            v = q.popleft()
            for w in self.G[v]:
                if w not in self.visited:
                    q.append(w)
                    self.visited.add(w)
                    self.edge_to[w] = v            

    def has_path_to(self,v):
        return v in self.visited
    
    def path_to(self,v):
        if v in self.visited:
            path = []
            x = v
            while x != self.s:
                path.append(x)
                x = self.edge_to[x]
            path.append(x)
        return path
 