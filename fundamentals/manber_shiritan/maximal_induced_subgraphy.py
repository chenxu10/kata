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

if __name__ == '__main__':
    main()
