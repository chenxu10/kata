#DONE: TCR workflow
#DONE: Functional Programming
#TODO: Concurrency
#TODO: primetodfssearch
#TODO: OCaml
#TODO: Reverse(SquareRootSCIP)
#TODO: Cryptography
#TODO: Quantum Computing

import pytest
import math

def primefactor(x):
    sol = []
    divisor = 2
    while x > 1:
        while x % divisor == 0:
            sol.append(divisor)
            x //= divisor
        divisor += 1
    return sol
    
def primefactor_functional(x):
    primes = []

    def helper(x,i):
        # base case
        if i > int(math.sqrt(x)):
            primes.append(x)
            return

        if x % i != 0:
            helper(x,i+1)
        else:
            primes.append(i)
            helper(x/i, i)
            
    helper(x,2)
    return primes

class TestPrimeFactor:
    def test_primefactor(self):
        #assert primefactor_functional(1) == []
        assert primefactor_functional(2) == [2]
        assert primefactor_functional(3) == [3]
        assert primefactor_functional(4) == [2,2]
        assert primefactor_functional(8) == [2,2,2]
        assert primefactor_functional(9) == [3,3]
        assert primefactor_functional(2 * 3 * 5 * 7) == [2,3,5,7]


def print_square_under(x):
    return list(map(lambda x:x*x, range(1,x+1)))

class TestPrintSquare:
    def test_printsquare_under(x):
        assert print_square_under(1) == [1]
        assert print_square_under(3) == [1,4,9]
        assert print_square_under(5) == [1,4,9,16,25]
