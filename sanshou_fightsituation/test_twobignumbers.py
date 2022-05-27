"""
Calculate the result for the mutiplication for two big numbers 
(big number means the number is even larger than type long). 
You can assume input is two long type arrays. Every array can be seen as a big number.
"""

def two_big_number(num1, num2):
    n1 = len(num1)
    n2 = len(num2)
    res = [0] * (n1 + n2)

    for i in range(n1 - 1, -1, -1):
        for j in range(n2 - 1, -1, -1):
            p1 = i + j
            p2 = i + j + 1
            mul = num1[i] * num2[j]
            sum = mul + res[p2]
            res[p2] = sum % 10
            res[p1] += sum // 10

    i = 0
    while i < len(res) and res[i] == 0:
        i += 1


    newres = res[i:]
    return newres

def test_two_big_number():
    bignumber1 = [1,2]
    bignumber2 = [1]
    assert two_big_number(bignumber1,bignumber2) == [1,2]
    assert two_big_number([1,8],[3,4]) == [6,1,2]
    assert two_big_number([9,9,9],[9,9,9]) == [9,9,8,0,0,1]

# Related Problems: Leetcode43