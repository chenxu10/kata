def spiral_matrix(matrix):
    result = []
    x, y = 0, 0
    dirx, diry = 1, 0
    visited = set()
    rows = len(matrix)
    cols = len(matrix[0])
    count = rows * cols
    # spiral #switch the directions every time reach a corner      --->dirx
                                                                    #|
    #or ((x + dirx, y + diry) in visited)                                                            #|diry
    def time_to_rotate(x, y):
        turningpoint =  (x + dirx < 0) or \
            (x + dirx >= cols) or \
            (y + diry < 0) or \
            (y + diry >= rows) \
            or ((x + dirx, y + diry) in visited)
        return turningpoint

    while len(result) < count:
        result.append(matrix[y][x])
        visited.add((x,y))
        if time_to_rotate(x, y):
            dirx, diry = -diry, dirx
        x += dirx
        y += diry           
        
    return result 

def test_spiral_matrix():
    matrix = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]]
    real = spiral_matrix(matrix)
    expected = [1,2,3,4,8,12,11,10,9,5,6,7]
    print(real)
    assert real == expected

if __name__ == '__main__':
    test_spiral_matrix()


# Related problems leetcode 2326