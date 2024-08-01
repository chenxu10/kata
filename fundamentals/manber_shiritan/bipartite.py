


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
        if not visited[node]:
            if not dfs(node, 0):
                return False

    return True

def test_bipartite():
    G = {'A':['B','C'],
         'B':['A','D'],
         'C':['A','D'],
         'D':['B','C']}
    assert bipartite(G) == True

def main():
    test_bipartite()
if __name__ == '__main__':
    main()