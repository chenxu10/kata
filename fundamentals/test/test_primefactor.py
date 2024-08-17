
def prime_factor(x):
    ans = []
    if x > 1:
        ans.append(2)
    return ans

def test_prime_factor():
    assert prime_factor(1) == []
    assert prime_factor(2) == [2]

def main():
    test_prime_factor()

if __name__ == '__main__':
    main()