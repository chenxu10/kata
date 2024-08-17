"""
Adjacent Lists of Graph
"""

class G:
    def __init__(self, v):
        self.v = v
        self.e = 0
        self.adj_lists = [[] for i in range(v)]

    def _validate_vertex(self,v):
        if v < 0 or v >= self.v:
            raise ValueError(f"vertex {v} is not between 0 and vertices")

    def add_edge(self,v, w):
        self._validate_vertex(v)
        self._validate_vertex(w)
        self.adj_lists[v].append(w)
        self.adj_lists[w].append(v)
        self.e += 1

def test_adjacency_list_graph_structure():
    graph = G(4)
    graph.add_edge(1,2) #O(1)
    assert graph.e == 1
    assert (1 in i for i in graph.adj_lists)