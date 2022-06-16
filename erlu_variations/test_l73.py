
"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and
column to 0's. You must do it in place.
"""

def setzeros(matrix):
    """
    First put all indexes of matrices into two sets as long as : row and col,
    Then iterate through matrix again if row or col index are in two sets
    """
    rowset = set()
    colset = set()

    row = len(matrix)
    col = len(matrix[0])

    def zeroindices_to_sets(matrix, rowset, colset, row, col):
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    rowset.add(i)
                    colset.add(j)
    
    zeroindices_to_sets(matrix, rowset, colset, row, col)

    def update_zero(matrix, rowset, colset, row, col):
        for i in range(row):
            for j in range(col):
                if (i in rowset) or (j in colset):
                    matrix[i][j] = 0
    
    update_zero(matrix, rowset, colset, row, col)

    return matrix


# T:O(m*n)
# S:O(m+n)

def test_set0matrix():
    matrix = [[1, 1, 1], [1, 0, 0], [1, 0, 0]]
    expected = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert setzeros(matrix) == expected
