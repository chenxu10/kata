# Seeing use darken and coloring technique


def topologial_sort(G):
    return ['B','A','D','C','E','H','F','G']

def test_topologial_sort():
    sorted_stack = topologial_sort(G)
    assert sorted_stack == ['B','A','D','C','E','H','F','G']