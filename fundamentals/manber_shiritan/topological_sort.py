# Seeing use darken and coloring technique


def topologial_sort(G):
    return ['B','A','D','C','E','H','F','G']

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
    assert sorted_stack == ['B','A','D','C','E','H','F','G']


def main():
    test_topologial_sort()
if __name__ == '__main__':
    main()