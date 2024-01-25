from collections import Counter

def numberofgoodpaths(vals, edges):
    # biggest insights:maximum value is k, then path is k*(k-1)/2
    def edge_with_larger_value():
        res = sorted([max(vals[i],vals[j]), i, j] for i, j in edges)
        return res
    
    def find(x):
        if f[x] != x:
            f[x] = find(f[x])
        return f[x]
    
    res = n = len(vals)
    f = list(range(n))
    count = [Counter({vals[i]:1}) for i in range(n)]
    edges = edge_with_larger_value()

    for v, i, j in edges:
        fi, fj = find(i), find(j) #find
        ci, cj = count[fi][v], count[fj][v]
        res += ci * cj
        f[f[j]] = f[i] #union
        count[fi] = Counter({v:ci + cj})

    return res


def test_numberofgoodpaths():
    vals = [1,3,2,1,3]
    edges = [[0,1],[0,2],[2,3],[2,4]]
    result = numberofgoodpaths(vals, edges)
    expected = 6
    assert result == expected


if __name__=='__main__':
    vals = [1,3,2,1,3,4]
    edges = [[0,1],[0,2],[2,3],[2,4]]
    print(numberofgoodpaths(vals, edges))