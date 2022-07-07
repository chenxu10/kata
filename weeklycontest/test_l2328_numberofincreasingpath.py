from functools import lru_cache

def countpaths(matrix):
    m = len(matrix)
    n = len(matrix[0])

    def resultij(matrix, i, j):
        m = len(matrix)
        n = len(matrix[0])
        res = 1
        for x, y in [[i, j + 1], [i, j - 1], [i + 1, j], [i - 1, j]]:
            if 0 <= x < m and 0 <= y < n and matrix[x][y] < matrix[i][j]:
                res += resultij(matrix, x,y)
        return res

    return sumcellresult(matrix)

def sumcellresult(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = sum(resultij(matrix,i,j) for i in range(rows) for j in range(cols))
    return result

def resultij(matrix, i, j):
    m = len(matrix)
    n = len(matrix[0])
    res = 1
    for x, y in [[i, j + 1], [i, j - 1], [i + 1, j], [i - 1, j]]:
        if 0 <= x < m and 0 <= y < n and matrix[x][y] < matrix[i][j]:
            res += resultij(matrix, x,y)
    return res

def test_resultij():
    matrix = [[1,1],[2,4]]
    actual = resultij(matrix, 1, 1)
    expected = 4
    assert actual == expected
    
def test_sumcellresult():
    input = [[1,1],[2,4]]
    actual = sumcellresult(input)
    expected = 8
    assert actual == expected

def test_countpaths():
    matrix = [[1,1],[3,4]]
    actual = countpaths(matrix)
    expected = 8
    assert expected == actual

if __name__ == '__main__':
    print(resultij([[1,1],[2,4]],1,1))