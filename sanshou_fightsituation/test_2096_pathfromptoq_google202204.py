def closedIslands():
    # fill island with water using dfs
    # fill island with right, left, up and bottom
    # go through all points in matrix, update solution when it's land and update the soluion
    raise notImplementedError

def test_closedIslands():
    matrix = [[0,1,0],[1,0,1],[0,1,0]]
    assert closedIslands(matrix) == 2