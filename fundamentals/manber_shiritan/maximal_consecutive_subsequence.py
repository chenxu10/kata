




def mcs(x):
    return [3,4]


def test_maximal_consecutive_sequence():
    assert mcs([1,-2,-1,4,-1]) == [3,4]
    assert mcs([-3,-2,-1,4,5]) == [4,5]

def main():
    test_maximal_consecutive_sequence()    

if __name__ == '__main__':
    main()