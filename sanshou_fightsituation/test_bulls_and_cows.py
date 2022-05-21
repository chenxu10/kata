from collections import Counter

def getHint(secret: str, guess: str) -> str:
    A = sum(a==b for a, b in zip(secret, guess))
    B = Counter(secret) & Counter(guess)               
    bulls = A
    cows = sum(B.values()) - A
    return "{}A{}B".format(bulls, cows)