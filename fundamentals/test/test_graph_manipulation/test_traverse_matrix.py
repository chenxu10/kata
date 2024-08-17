
def traverse_matrix(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    

    def dfs(i,j,cur_index):
        # lead node
        if cur_index == len(word):
            return True
        # terminate backtrack logic
        if i < 0 or i >= rows or j < 0 or j >= cols:
            return False
        if visited[i][j] or matrix[i][j] != word[cur_index]:
            return False
        
        visited[i][j] = 1
        vectors = [(-1,0),(1,0),(0,1),(0,-1)]
        for v in vectors:
            i += v[0]
            j += v[1]
            if dfs(i,j,cur_index + 1):
                return True
        visited[i][j] = 0
        return False

    for i in range(rows):
        for j in range(cols):
            if dfs(i,j,0):
                return True
    return False

def test_traverse_matrix():
    #assert traverse_matrix([[]],'abc') == False
    print(traverse_matrix([['a','b'],['c','d']],'abc'))
    #assert traverse_matrix([['a','b'],['d','c']],'abc') == True

def main():
    test_traverse_matrix()

if __name__ == '__main__':
    main()