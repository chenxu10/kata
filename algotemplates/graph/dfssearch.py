from collections import defaultdict

class DepthFirstSearch():
    # raise NotImplementedError
    def __init__(self, Graph, src_node):
        self.cnt = 0
        self.is_marked = [False for _ in range(len(Graph) + 1)]
        self._dfs(Graph, src_node)

    def _dfs(self, G, src_node):
        self.cnt += 1
        self.is_marked[src_node] = True

        for neighbor in G[src_node]:
            if not self.is_marked[neighbor]:
                self._dfs(G, neighbor)

    def count(self):
        return self.cnt

def test_DepthFirstSearch():
    G = defaultdict(list)
    G[1].append(2)
    G[2].append(5)
    G[5].append(1)

    G[3].append(4)
    G[4].append(3)

    src_node = 1
    s = DepthFirstSearch(G, src_node)
    
    connected_nodes = []
    for v in range(1, len(G) + 1):
        if s.is_marked[v]:
            connected_nodes.append(v)

    if s.count() == len(G):
        print("connected!")
    else:
        print("no connected")
           
    return connected_nodes

# Extension: How to use this problem for multiple sources search in digraph?

if __name__ == '__main__':
    print(test_DepthFirstSearch())
