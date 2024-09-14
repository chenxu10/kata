from collections import defaultdict
from queue import deque


class BFS:
    def __init__(self,G,s) -> None:
        self.G = G
        self.s = s
        self.edge_to = []
        self.visited = set()
        self._bfs_traverse()

    def _bfs_traverse(self):
        q = deque([self.s])
        while q:
            node = q.popleft()
            for nei in self.G[node]:
                if nei not in self.visited:
                    q.append(node)
                    self.visited.add(node)
                    self.edge_to.append(node)            

    def has_path_to(self,v):
        return v in self.visited
    
    def path_to(self,v):
        pass

def test_bfs_traverse():
    """
    #  A
    # / \
    #B   C
    #|   |
    #D---E
    """
    G = defaultdict()
    G['A'] = ['B','C']
    G['B'] = ['D']
    G['C'] = ['E']    
    bfs = BFS(G,'A')
    assert bfs.has_path_to('D') == True
    #assert bfs.path_to('D') == []

