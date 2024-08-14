# The Problem:

# Tricks:
# Reduce the size of the problem by eliminating elements from a set. Therefore,
# we try to find the eaisiest way to remove an element without changing the conditions
# of the problem.

'''
Mapping:
1 -> 3
2 -> 1
3 -> 1
4 -> 5
5 -> 5
6 -> 4
7 -> 6
'''

from collections import deque
def Algorithm_Mapping(f,n):
    S = [i for i in range(n)]
    c = [0 for _ in range(n)]
    q = deque()

    for i in range(n):
        c[f[i]] += 1

    for i in range(n):
        if c[i] == 0:
            q.append(i)

    while q:
        element = q.pop()
        S.remove(element)
        c[f[element]] -= 1
        if c[f[element]] == 0:
            q.append(f[element])

    return S
