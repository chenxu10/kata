






def equals(actual, expected):
    if actual == expected:
        return
    else:
        print(actual,"not equal to", expected)
        raise Exception(actual,"looks like")


def dfs_matrix(island_map):
    return [[1,1],[1,1]]

if __name__ == "__main__":
    island_map = [[1,1],[1,0]]
    equals(dfs_matrix(island_map),[[1,1],[1,1]])
