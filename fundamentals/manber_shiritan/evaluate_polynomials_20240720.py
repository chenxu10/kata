"""
Given a sequence of real numbers an, an-1, an-2, a1, a0
and a real number x. compute the polynomial Pn(x)=anx^n +an-1x^n-1 +a2x^2+... a1x+a0

Pn-1(x) =  an-1x^n-1 +a2x^2+... a1x+a0
Pn(x) = x*an + Pn-1(x)

Pn-1(x) = anx^n-1 + an-1x^n-2 + ... +a1
Pn(x) = x* Pn-1(x) + a0
"""

def compute_polynomial(alists,x):
    pn = alists[-1]

    for i in range(1, len(alists)):
        a0 = alists[-1 - i]        
        pn = x* pn + a0

    return pn

def test_compute_polynomial():
    #assert compute_polynomial([1],1) == 1
    #assert compute_polynomial([1,1],2) == 3
    assert compute_polynomial([3,2,1],2) == 3 + 2 * 2 + 1 * 4
    #assert compute_polynomial([3,2,1],2) == 3 * (2*2) + 2 * (2*1) + 1
    #assert compute_polynomial([1,2,2,1],1) == 1 * 1 + 2 * 1 * 1 + 2 * 1 + 1    

def main():
    test_compute_polynomial()

if __name__ == '__main__':
    main()
 