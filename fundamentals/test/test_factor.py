def fact(n):
    if n <= 1:
        return 1
    else:
        return fact(n - 1) * n

def test_fact():
    assert fact(1) == 1
    assert fact(3) == 3 * 2 * 1

if __name__ == "__main__":
    test_fact()