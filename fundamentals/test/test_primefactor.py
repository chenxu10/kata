
def prime_factor(x):
    ans = []
    if x > 1:
        ans.append(x)
        
    return ans
def test_prime_factor():
    assert prime_factor(1) == []
    assert prime_factor(2) == [2]
    # assert prime_factor(2) == [2]
    # assert prime_factor(3) == [3]
    # assert prime_factor(4) == [2,2]
    # assert prime_factor(5) == [5]
    # assert prime_factor(6) == [2,3]
    # assert prime_factor(8) == [2,2,2]

def main():
    test_prime_factor()

if __name__ == '__main__':
    main()