import math

def subarrayGCD():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        for j in range(i, n):
            if gcd(a[i], a[j]) == 1:
                return True
    return False

def gcd(x):
    res = 1
    maxx = max(x)
    for i in range(1, maxx+1):
        if all([j % i == 0 for j in x]):
            res = max(res, i)
    return res

if __name__ == '__main__':
    print(gcd([14,6,2]))