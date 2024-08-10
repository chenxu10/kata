def mcs(x):
    """
    decoupling finding new maximum and new maximum suffix
    """
    n = len(x)
    global_max = 0
    local_max = 0
    
    for i in range(n):
        if x[i] + local_max > global_max:
            local_max = x[i] + local_max
            global_max = local_max
        elif x[i] + local_max > 0:
            local_max = x[i] + local_max
        else:
            local_max = 0
        
    return global_max

def mcs_recursive(x):
    global_max = 0
    local_max = 0    
    
    def dfs(x, i=0):
        nonlocal local_max
        nonlocal global_max
        if i == len(x) - 1:
            return global_max
        elif x[i] + local_max > global_max:
            local_max = x[i] + local_max
            global_max = local_max
        elif x[i] + local_max > 0:
            local_max = x[i] + local_max
        else:
            local_max = 0
        return dfs(x, i + 1)

    return dfs(x, 0)

def test_maximal_consecutive_sequence():
    assert mcs([1,-2,-1,4,5]) == 4 + 5
    # context: running across negative number suffix decreasing
    assert mcs([1.5,-1,3,-2,-3,3]) == 1.5 - 1 + 3
    assert mcs_recursive([1.5,-1,3,-2,-3,3]) == 1.5 - 1 + 3

def main():
    test_maximal_consecutive_sequence()    

if __name__ == '__main__':
    main()