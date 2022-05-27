def townjudge(n, trust):
    graph = [0] * n
    for a, b in trust:
        graph[a] -= 1
        graph[b] += 1

    for index, item in enumerate(graph):
        if item == n - 1:
            return index + 1
    
    return -1