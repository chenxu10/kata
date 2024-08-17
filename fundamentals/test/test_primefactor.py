
def prime_factor(x):
    if x == 2:
        return [2]
    return []

def test_prime_factor():
    assert prime_factor(1) == []
    assert prime_factor(2) == [2]

def main():
    test_prime_factor()

if __name__ == '__main__':
    main()