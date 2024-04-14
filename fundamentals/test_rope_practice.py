class Rope:
    def substring(self, start, length):
        return Substring(self, start, length)

class String(Rope):
    def __init__(self, s):
        self.s = s
    
    def __str__(self):
        return self.s
        
class Substring(Rope):
    def __init__(self,rope, start, length):
        self.rope = rope
        self.start = start
        self.length = length
    
    def __str__(self):
        return str(self.rope)[self.start:self.start + self.length]
 
def to_rope(x):
    return String(x)

def expect(actual, expected):
    if actual == expected:
        return
    else:
        Exception("actual not equal to exp, looks like this",actual)

if __name__ == '__main__':
    expect(str(to_rope("abc")),"abc")
    expect(str(to_rope("abcde").substring(1,3).substring(1,1)),"c")
    expect(str(to_rope("abcdefg").substring(1,3).substring(1,2).substring(1,1)),"d")
