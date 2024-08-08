




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
    # assert mcs([1,-2,-1,4,-1]) == [3,4]
    # assert mcs([-3,-2,-1,4,5]) == [4,5]
    pass

def main():
    print(mcs([1,-2,-1,4,5]))
    print(mcs([2,-3,1.5,-1,-3,-2,-3,3]))
    #test_maximal_consecutive_sequence()    

if __name__ == '__main__':
    main()