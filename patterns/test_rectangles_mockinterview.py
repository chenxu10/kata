from collections import defaultdict
def numberofrects(points):
    """
    # (x1,y1),(x2,y2),(x3,y3),(x4,y4)
    # x1 != x2 and y1 == y2
    # x1 != x4 and y1 != y4
    (0,0)   2   3

    (0,1)   5   6
    """
    ans = 0
    count = defaultdict(int)
    for p in points:
        for p_above in points:
            x = p[0]
            y = p[1]
            x_above = p_above[0]
            y_above = p_above[1]
            if x == x_above and y < y_above:
                y_pair = (y, y_above) # (0,1)
                ans += count[y_pair]  # 1
                count[y_pair] += 1
    return ans

def test_numberofrects():
    assert numberofrects([(0,0),(0,1),(0,2),(1,0),(1,1),(1,2)]) == 3
    assert numberofrects([
        (0,0),(0,1),(0,2),
        (1,0),(1,1),(1,2),
        (2,0),(2,1),(2,2)]) == 9
    N = 7
    ob = [0] * N
    ob[0] = [0, 0]
    ob[1] = [1, 0]
    ob[2] = [1, 1]
    ob[3] = [0, 1]
    ob[4] = [2, 0]
    ob[5] = [2, 1]
    ob[6] = [11, 23]
    assert numberofrects(ob) == 3

 