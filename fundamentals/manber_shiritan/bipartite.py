


def bipartite(G):
    visited = {node:False for node in G}
    color = {'not_color':-1,'blue':0,'orange':1}

    def bfs(node):
        pass

    for node in G:
        if not visited[node]:
            bfs(node)

    return True

def test_bipartite():
    G = {'A':['B','C'],
         'B':['A','C'],
         'C':['A','D'],
         'D':['B','C']}
    assert bipartite(G) == True

def main():
    test_bipartite()
if __name__ == '__main__':
    main()