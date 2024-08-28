import pytest

def max_swap(num):
    # Convert number to list of digits
    digits = list(str(num))
    n = len(digits)
    
    # Find the rightmost occurrence of each digit
    last_occurrence = {d: i for i, d in enumerate(digits)}
    
    for i in range(n):
        for d in range(9, int(digits[i]), -1):
            if str(d) in last_occurrence and last_occurrence[str(d)] > i:
                # Swap digits
                digits[i], digits[last_occurrence[str(d)]] = digits[last_occurrence[str(d)]], digits[i]
                return int(''.join(digits))
    
    # No swap needed
    return num

# ... (keep the TestMaxSwap class and unittest.main() call)

def test_max_swap():
    assert max_swap(2736) == 7236
    assert max_swap(9973) == 9973

if __name__ == '__main__':
    test_max_swap()
