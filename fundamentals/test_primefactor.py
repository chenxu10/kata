import pytest

def primefactor(n:int):
    factors = []
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    return factors

class TestPrimeFacor():
    assert primefactor(1) == []
    assert primefactor(2) == [2]
    assert primefactor(3) == [3]
    assert primefactor(4) == [2,2]
    assert primefactor(5) == [5]
    assert primefactor(6) == [2,3]
    assert primefactor(8) == [2,2,2]
    assert primefactor(9) == [3,3]

def primefactor(n:int):
    factors = []
    if n > 1:
        if n % 2 == 0:
            factors.append(2)
            n //= 2
        if n > 1:
            factors.append(n)
    return factors

class TestPrimeFacor:
    def test_primefactor(self):
        assert primefactor(1) == []
        assert primefactor(2) == [2]
        assert primefactor(3) == [3]
        assert primefactor(4) == [2,2]