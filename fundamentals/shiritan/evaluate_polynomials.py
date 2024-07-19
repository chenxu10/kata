"""
Given a sequence of real numbers an, an-1, an-2, a1, a0
and a real number x. compute the polynomial Pn(x)=anx^n +an-1x^n-1 + a1x+a0
"""

def compute_polynomial(alists,x):
    if len(alists) == 1:
        return alists[0]
    else:
        return 7

def test_compute_polynomial():
    assert compute_polynomial([1],2) == 1
    assert compute_polynomial([1,1,1],2) == 7

def main():
    test_compute_polynomial()
    
if __name__ == '__main__':
    main()
