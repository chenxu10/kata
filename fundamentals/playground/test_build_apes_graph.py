"""
Implementation of p154 of chimpanzee politics
"""
from collections import defaultdict, namedtuple

def build_graph():
    match_chimp = namedtuple('connectchimp',('chimp1','chimp2'))
    match_chimps = []
    match_chimp.chimp1 = 'Luit'
    match_chimp.chimp2 = 'Yeron'
    match_chimps.append(match_chimp)
    graph = defaultdict(set)
    
    for chimps in match_chimps:
        graph[chimps.chimp1].add(chimps.chimp2)
        print(graph)       
    return graph
 
if __name__ == '__main__':
    graph = build_graph()
#    assert graph['Luit'] == set(['Nikkie','Yeron'])