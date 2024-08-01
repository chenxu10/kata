# Seeing use darken and coloring technique
#https://www.youtube.com/watch?v=eL-KzMXSXXI
from collections import deque

def topologial_sort(G):
    stack = deque()
    visited = {node:False for node in G}
    
    def dfs(node):
        visited[node] = True

        for nei in G[node]:
            if not visited[nei]:
                dfs(nei)

        stack.appendleft(node)

    for vertex in G:
        print(vertex)
        if not visited[vertex]:
            dfs(vertex)

    return list(stack)
   
def test_topologial_sort():
    G = {
        'A':['C'],
        'B':['C','D'],
        'C':['E'],
        'D':['F'],
        'E':['H','F'],
        'F':['G'],
        'G':[],
        'H':[]
    }
    sorted_stack = topologial_sort(G)
    print(sorted_stack)
    assert sorted_stack == ['B', 'D', 'A', 'C', 'E', 'F', 'G', 'H']


def main():
    test_topologial_sort()
if __name__ == '__main__':
    main()