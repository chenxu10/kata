from collections import defaultdict






class BFS:
    def __init__(self,G,s) -> None:
        self.G = G
        self.s = s
        self.edge_to = []

    def has_path_to(self,v):
        return True
    
    def path_to(self,v):
        return ['A','B','D']


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
    G['B'] = ['D']
    G['C'] = ['E']    
    bfs = BFS(G,'A')
    assert bfs.has_path_to('D') == True
    assert bfs.path_to('D') == []

