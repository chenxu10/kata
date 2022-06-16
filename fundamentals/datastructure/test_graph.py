from utils import UndirectedGraph

def test_graph_counts():
    adjtxtblk = """
      A:  E B 
      B:  E A F 
      C:  D F 
      D:  C G H 
      E:  A B 
      F:  C G B 
      G:  D H F 
      H:  G D 
    """
    graph = UndirectedGraph(adjtxt=adjtxtblk)
    assert graph.num_nodes == 8 
    assert graph.num_edges == 10

