"""
Implementation of p154 of chimpanzee politics
"""

def build_graph():
    graph = {'Luit':set(['Nikkie','Yeron'])}
    return graph

if __name__ == '__main__':
    graph = build_graph()
    assert graph['Luit'] == set(['Nikkie','Yeron'])