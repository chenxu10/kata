from functools import lru_cache


def counterpaths_2(grid):
    m = len(grid)
    n = len(grid[0])
    mod = 10 ** 9 + 7

    @lru_cache
    def result(i,j):
        """
        Number of increasing path end at i, j
        """
        res = 1
        for x, y in [(i - 1,j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if 0 <= x < m and 0 <= y < n and grid[x][y] < grid[i][j]:
                res += result(x,y) % mod

        return res

    return  sum(result(i,j) for i in range(m) for j in range(n)) % mod


def countpaths(grid):
    m = len(grid)
    n = len(grid[0])

    def resultij(grid, i, j):
        m = len(grid)
        n = len(grid[0])
        res = 1
        for x, y in [[i, j + 1], [i, j - 1], [i + 1, j], [i - 1, j]]:
            if 0 <= x < m and 0 <= y < n and grid[x][y] < grid[i][j]:
                res += resultij(grid, x,y)
        return res

    return sumcellresult(grid)

def sumcellresult(grid):
    rows = len(grid)
    cols = len(grid[0])
    result = sum(resultij(grid,i,j) for i in range(rows) for j in range(cols))
    return result

def resultij(grid, i, j):
    m = len(grid)
    n = len(grid[0])
    res = 1
    for x, y in [[i, j + 1], [i, j - 1], [i + 1, j], [i - 1, j]]:
        if 0 <= x < m and 0 <= y < n and grid[x][y] < grid[i][j]:
            res += resultij(grid, x,y)
    return res

def test_resultij():
    grid = [[1,1],[2,4]]
    actual = resultij(grid, 1, 1)
    expected = 4
    assert actual == expected
    
def test_sumcellresult():
    input = [[1,1],[2,4]]
    actual = sumcellresult(input)
    expected = 8
    assert actual == expected

def test_countpaths():
    grid = [[1,1],[3,4]]
    actual = countpaths(grid)
    expected = 8
    assert expected == actual

def test_countpaths_2():
    grid = [[1,1],[3,4]]
    actual = counterpaths_2(grid)
    expected = 8
    assert expected == actual

if __name__ == '__main__':
    print(resultij([[1,1],[2,4]],1,1))