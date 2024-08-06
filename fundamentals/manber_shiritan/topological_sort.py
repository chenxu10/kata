# Seeing use darken and coloring technique
#https://www.youtube.com/watch?v=eL-KzMXSXXI
from collections import deque

def topologial_sort(G):
    def init_visit_status():
        # 0 for unvisited, 1 for visiting and 2 for visited
        visited = {node:0 for node in G}
        has_cycle = [False]
        return visited, has_cycle

    def dfs(node):
        if has_cycle[0]:
            return 
        visited[node] = 1
        for nei in G[node]:
            if visited[nei] == 1:
                has_cycle[0] = True
            if visited[nei] == 0 and not has_cycle[0]:
                dfs(nei)
        visited[node] = 2
        stack.appendleft(node)

    def traverse_graph():
        for vertex in G:
            if not visited[vertex]:
                dfs(vertex)
                if not has_cycle[0]:
                    return list(stack)

    stack = deque()
    visited, has_cycle = init_visit_status()    
    traverse_graph()

    return []

    
    
def test_topologial_sort():
    # G = {
    #     'A':['C'],
    #     'B':['C','D'],
    #     'C':['E'],
    #     'D':['F'],
    #     'E':['H','F'],
    #     'F':['G'],
    #     'G':[],
    #     'H':[]
    # }
    # sorted_stack = topologial_sort(G)
    # print(sorted_stack)
    # assert sorted_stack == ['B', 'D', 'A', 'C', 'E', 'F', 'G', 'H']

    G1 = {'A':'B','B':'C','C':'A'}
    sorted_stack = topologial_sort(G1)
    print(sorted_stack)
    assert sorted_stack == []

def main():
    test_topologial_sort()
if __name__ == '__main__':
    main()