from collections import defaultdict

def find_k_core(graph, k):
    # Create a copy of the graph
    H = graph.copy()
    
    # Get the degree of each vertex
    degree = defaultdict(int)
    for u, v in H:
        degree[u] += 1
        degree[v] += 1
    # Create a queue of vertices with degree < k
    queue = [v for v in degree if degree[v] < k]
    
    while queue:
        # Remove v and its incident edges
        v = queue.pop(0)
        H = [(u,w) for u, w in H if u!=v and w!=v]
        
        # Update degrees based on neighbors
        neighbors = [u for u, w in H if w != v]
        for u in neighbors:
            degree[u] -= 1
            if degree[u] < k:
                queue.append(u)

        del queue[v]
    
    return H if H else None

def main():
    graph = [(0, 1), (0, 2), (1, 2), (2, 3), (3, 4), (4, 5), (5, 3)]
    k = 2
    result = find_k_core(graph, k)
    assert result == [(0, 1), (0, 2), (1, 2), (2, 3), (3, 4), (4, 5), (5, 3)]


# Related problems
# Topological Sort
# Coloring Problem(Whether a graph is bipartite)

# Seeing use darken and coloring technique
#https://www.youtube.com/watch?v=eL-KzMXSXXI
from collections import deque

def topologial_sort(G):
    def dfs(node):
        if has_cycle[0]:
            return
    
        visited[node] = 0

        for nei in G[node]:
            if visited[nei] == -1 and has_cycle[0] == False:
                dfs(nei)
            if visited[nei] == 0:
                has_cycle[0] = True

        visited[node] = 1
        stack.appendleft(node)
  
    
    visited = {node:-1 for node in G}
    stack = deque() 
    has_cycle = [False]
    
    for node in G:
        if (visited[node]==-1):
            dfs(node)
            if has_cycle[0] == True:
                return None
            
    return list(stack)
    
def test_topologial_sort():
    G = {
        'A':['B'],
        'B':['C'],
        'C':['A']
    }
    sorted_stack = topologial_sort(G)
    print(sorted_stack)
    #assert sorted_stack == ['B', 'D', 'A', 'C', 'E', 'F', 'G', 'H']

    # G1 = {'A':'B','B':'C','C':'A'}
    # sorted_stack = topologial_sort(G1)
    # assert sorted_stack == []

test_topologial_sort()


def bipartite(G):
    visited = {node:False for node in G}
    color = {node:-1 for node in G}

    def dfs(node, c):
        "color two different colors in an edge"
        visited[node] = True
        color[node] = c

        for nei in G[node]:
            if (not visited[nei]) and (not dfs(nei, 1 - c)):
                return False
            elif color[nei] == color[node]:
                return False           
        return True

    for node in G:
        if (not visited[node]) and (not dfs(node, 0)):
            return False

    return True

def test_bipartite():
    G = {'A':['B','C'],
         'B':['A','D'],
         'C':['A','D'],
         'D':['B','C']}
    assert bipartite(G) == True

test_bipartite()
