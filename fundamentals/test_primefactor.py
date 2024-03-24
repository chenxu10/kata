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
    ans = []
    if n == 1:
        return ans
    if n == 2:
        ans.append(2)
        return ans
    else:
        ans.append(n // 2)
        primefactor(n // 2)  

class TestPrimeFacor:
    def test_primefactor(self):
        assert primefactor(1) == []
        assert primefactor(2) == [2]
        #assert primefactor(3) == [3]
        assert primefactor(4) == [2,2]