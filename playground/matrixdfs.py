"""
Game of life
"""


def equals(actual, expected):
    if actual == expected:
        return
    else:
        print(actual,"not equal to", expected)
        raise Exception("actual looks like this", actual)


def dfs_matrix(island_map):
    # 1 1
    # 1 0
    def dfs_matrix_help(island_map, x, y, m, n):
        # update island map
        direction_vector = [(1,0),(0,1),(1,1)]
        for i, j in direction_vector:
            x += i
            y += j
            if (0 <= x < m and 0 <= y < n) and island_map[x][y] == 0:
                island_map[x][y] = 1    
    m = len(island_map)
    n = len(island_map[0])
    x = 0
    y = 0
    dfs_matrix_help(island_map, x, y, m, n)
    return island_map
    

if __name__ == "__main__":
    island_map = [[1,1],[1,0]]
    equals(dfs_matrix(island_map),[[1,1],[1,1]])
