"""
# Python program for
# implementation of Horner Method 
# for Polynomial Evaluation
 
# returns value of poly[0]x(n-1)
# + poly[1]x(n-2) + .. + poly[n-1]
"""

def compute_polynomial(alists,x):
    pn = alists[0] #an

    for i in range(1, len(alists)):
        ai = alists[i]        
        pn = x * pn + ai

    return pn

def test_compute_polynomial():
    assert compute_polynomial([2, 0, 3, 1],2) == 2 * (2**3) + 0 + 3 * 2 + 1

def main():
    test_compute_polynomial()

# Related problems 1634

if __name__ == '__main__':
    main()
 