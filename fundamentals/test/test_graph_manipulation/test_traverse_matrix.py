
def traverse_matrix(matrix, word):
    rows = len(matrix)
    cols = len(matrix[0])
   

    def dfs(i,j,cur_index):
        # lead node
        if cur_index == len(word):
            return True
        # terminate backtrack logic
        if i < 0 or i >= rows or j < 0 or j >= cols:
            return False
        if matrix[i][j] != word[cur_index]:
            return False
        
        temp = matrix[i][j]
        matrix[i][j] = '#'
        result = dfs(i+1, j, cur_index+1) or dfs(i-1, j, cur_index+1) or dfs(i, j+1, cur_index+1) or dfs(i, j-1, cur_index+1)
        matrix[i][j] = temp
        return result

    for i in range(rows):
        for j in range(cols):
            if dfs(i,j,0):
                return True
    return False

def test_traverse_matrix():
    #assert traverse_matrix([[]],'abc') == False
    print(traverse_matrix([['a','b'],['d','c']],'abc'))
    #assert traverse_matrix([['a','b'],['d','c']],'abc') == True

def main():
    #
    test_traverse_matrix()

if __name__ == '__main__':
    main()