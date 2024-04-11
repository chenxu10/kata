class Rope:
    def __init__(self, s):
        self.s = s
    
    def __str__(self):
        return self.s

    def substring(self, start, length):
        return Substring(self, start, length)
        
class Substring:
    def __init__(self,rope, start, length):
        self.rope = rope
        self.start = start
        self.length = length
    
    def __str__(self):
        return str(self.rope)[self.start:self.start + self.length]

def to_rope(x):
    return Rope(x)

if __name__ == '__main__':
    assert str(to_rope("abc")) == "abc"
    assert str(to_rope("abcde").substring(1,3)) == "bcd"
