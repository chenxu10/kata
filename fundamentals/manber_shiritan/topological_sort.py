# Seeing use darken and coloring technique

from collections import deque

def topologial_sort(G):
    stack = deque()
    visted = {node:False for node in G}

    def dfs(node):
        visted[node] = True

        for nei in G[node]:
            if not visted[nei]:
                dfs(nei)

        stack.appendleft(node)

    for vertex in G:
        if vertex not in visted:
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
    #assert sorted_stack == ['B','A','D','C','E','H','F','G']


def main():
    test_topologial_sort()
if __name__ == '__main__':
    main()