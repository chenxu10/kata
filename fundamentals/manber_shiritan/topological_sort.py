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
        if (visited[node]==-1) and has_cycle[0] == False:
            dfs(node)
            
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

    # G1 = {'A':'B','B':'C','C':'A'}
    # sorted_stack = topologial_sort(G1)
    # assert sorted_stack == []

def main():
    test_topologial_sort()

if __name__ == '__main__':
    main()