"""
Implementation of p154 of chimpanzee politics
"""
from collections import defaultdict, namedtuple

def build_graph():
    match_chimp = namedtuple('connectchimp',('Luit','Tepel'))
    match_chimps = []
    match_chimps.append(match_chimp)
    graph = defaultdict(set)
    for chimps in match_chimps:
        print(chimps)
    return graph
 
if __name__ == '__main__':
    graph = build_graph()
#    assert graph['Luit'] == set(['Nikkie','Yeron'])