# The key of this problem is to eliminate elements not contributing

MATRIX = [[ 1, 1, 0 ],
          [ 0, 1, 0],
          [ 1, 1, 1]]
 

MATRIX = [[ 1, 0],
          [ 1, 1]]

def knows(a, b):
    return MATRIX[a][b]


def findCelebrity(n):
    s = []
    
    for i in range(n):
        s.append(i)

    # Eliminate the problem size by reducing non-celebrity
    while len(s) > 1:
        A = s.pop()
        B = s.pop()
        if knows(A, B):
            s.append(B)
        else:
            s.append(A)

    if len(s) == 0:
        return -1

    C = s.pop()
    if knows(C,B):
        C = B
    
    if knows(C,A):
        C = A
    
    # Check if C is actually
    # a celebrity or not
    for i in range(n):
     
        # If any person doesn't
        # know 'a' or 'a' doesn't
        # know any person, return -1
        if ((i != C) and
           (knows(C, i) or
           not(knows(i, C)))):
            return -1
 
    return C
    
def test_find_celebrity():
    # assert findCelebrity(3) == 1
    assert findCelebrity(2) == 0


if __name__ == '__main__':
    test_find_celebrity()


# Related problems
# Leetcode 227/997(indegree vs outdegree)