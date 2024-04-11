"""
Implementation of p154 of chimpanzee politics
"""
from collections import defaultdict, namedtuple

def build_graph():
    namedtuple('connectchimp',('Luit','Tepel'))
    graph = defaultdict(set)
    graph['Luit'] = set(['Nikkie','Yeron'])
    return graph
 
if __name__ == '__main__':
    graph = build_graph()
    assert graph['Luit'] == set(['Nikkie','Yeron'])