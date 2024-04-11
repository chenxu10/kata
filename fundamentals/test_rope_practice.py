









class Rope:
    def __init__(self, s):
        self.s = s
    
    def __str__(self):
        return self.s

    def substring(self, start, length):
        self.s = self.s[start: start + length]

def to_rope(x):
    return Rope(x)

if __name__ == '__main__':
    assert str(to_rope("abc")) == "abc"
    print(str(to_rope("abcde").substring(1,3)))
