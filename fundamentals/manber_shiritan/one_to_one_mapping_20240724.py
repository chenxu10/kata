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

import queue
def Algorithm_Mapping(f,n):
    S = [i for i in range(n)]
    
    c = [0 for i in range(n)]
    for i in range(n):
        c[f[i]] += 1
    
    Queue = queue.Queue()
    for j in range(n):
        if c[j] == 0:
            Queue.put(j)
    
    while not Queue.empty():
        i = Queue.get()
        S.remove(i)
        c[f[i]] -= 1
        if c[f[i]] == 0: 
            Queue.put(f[i])      
    return S

f = [2, 0, 0, 4, 4, 3, 5]
n = 7
print(Algorithm_Mapping(f,n))