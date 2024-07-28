# Seeing use darken and coloring technique
#https://www.youtube.com/watch?v=eL-KzMXSXXI
from collections import deque

def topologial_sort(G):
    visited = {node:False for node in G}
    stack = deque()

    def dfs(node):
        visited[node] = True

        for node in visited:
            if not visited[node]:
                dfs(node)

            


    for node in G:
        if not visited[node]:
            dfs(node)

    return stack
   
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