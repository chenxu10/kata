"""
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

Input: n = 2, trust = [[1,2]]
Output: 2
"""

def townjudge(n, trust):
    graph = [0] * n
    for a, b in trust:
        graph[a] -= 1
        graph[b] += 1

    for index, item in enumerate(graph):
        if item == n - 1:
            return index + 1
    
    return -1