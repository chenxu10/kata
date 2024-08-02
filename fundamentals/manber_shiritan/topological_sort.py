# Seeing use darken and coloring technique
#https://www.youtube.com/watch?v=eL-KzMXSXXI
from collections import deque

def topologial_sort(G):
    def init_visit_status():
        # 0 for unvisited, 1 for visiting and 2 for visited
        visited = {node:0 for node in G}
        return visited

    def dfs(node):
        visited[node] = 1
        for nei in G[node]:
            if visited[nei] == 1:
                print("has cycle")
            if visited[nei] == 0:
                dfs(nei)
        visited[node] = 2
        stack.appendleft(node)

    def traverse_graph():
        for vertex in G:
            if not visited[vertex]:
                dfs(vertex)

    stack = deque()
    visited = init_visit_status()    
    traverse_graph()

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