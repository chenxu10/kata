from fundamentals.mianjing.fb_lc_62_20240902 import unique_paths
from fundamentals.mianjing.fb_lc_62_20240902 import unique_paths_graph

def test_unique_paths():
    assert unique_paths(3, 7) == 28
    assert unique_paths(3, 2) == 3

def test_unique_paths_graph():
    assert unique_paths_graph(3, 7) == 28
    assert unique_paths_graph(3, 2) == 3

test_unique_paths()
test_unique_paths_graph()
