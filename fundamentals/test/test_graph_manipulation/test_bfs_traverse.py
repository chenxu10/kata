from collections import defaultdict
from fundamentals.dsalgo.graph.bfs_find_path import BFS

def test_bfs_traverse():
    """
    #  A
    # / \
    #B   C
    #|   |
    #D---E
    """
    G = defaultdict()
    G['A'] = ['B','C']
    G['B'] = ['D','A']
    G['C'] = ['E','A']
    G['D'] = ['B']
    G['E'] = ['C']    
    print(G)
    bfs = BFS(G,'A')
    print(bfs.has_path_to('C'))
    print(bfs.path_to('C'))
    #assert bfs.has_path_to('D') == True
    #assert bfs.path_to('D') == []

test_bfs_traverse()

