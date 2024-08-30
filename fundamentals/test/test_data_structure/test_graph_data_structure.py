"""
Adjacent Lists of Graph

Related problems find the town judge and find the celebrity
"""

class G:
    def __init__(self, v):
        self.v = v
        self.e = 0
        self.adj_lists = [[] for _ in range(v)]

    def add_edge(self, v, w):
        self._is_valid(v)
        self._is_valid(w)
        self.adj_lists[v].append(w)
        self.adj_lists[w].append(v)
        self.e += 1

    def _is_valid(self,v):
        if v < 0 or v >= len(self.adj_lists):
            raise ValueError("Invaid v")

def test_adjacency_list_graph_structure():
    graph = G(4)
    graph.add_edge(1,2) #O(1)
    assert graph.e == 1
    assert (1 in i for i in graph.adj_lists)

class Graph:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.adj_list = {}
        self._build_graph()

    def _build_graph(self):
        for i in range(self.rows):
            for j in range(self.cols):
                node = (i, j)
                self.adj_list[node] = []
                if i < self.rows - 1:
                    self.adj_list[node].append((i+1, j))
                if j < self.cols - 1:
                    self.adj_list[node].append((i, j+1))

    def dfs(self, start, end, path, paths):
        if start == end:
            paths.append(path)
            return
        for neighbor in self.adj_list[start]:
            self.dfs(neighbor, end, path + [neighbor], paths)

def unique_paths_graph(m, n):
    graph = Graph(m, n)
    start = (0, 0)
    end = (m-1, n-1)
    paths = []
    graph.dfs(start, end, [start], paths)
    return len(paths)

# Test
print(unique_paths_graph(3, 7))  # Should print 28