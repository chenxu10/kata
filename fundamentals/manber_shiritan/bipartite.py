


def bipartite(G):
    visited = {node:False for node in G}
    color = {node:-1 for node in G}
    
    
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