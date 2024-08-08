



def mcs(x):
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


def test_maximal_consecutive_sequence():
    assert mcs([1,-2,-1,4,5]) == 9
    assert mcs([2,-3,1.5,-1,3,-2,-3,3]) == 3.5

def main():
    test_maximal_consecutive_sequence()    

if __name__ == '__main__':
    main()