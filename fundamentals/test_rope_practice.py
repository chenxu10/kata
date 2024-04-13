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


def equals(rope, expected):
    actual = str(rope)
    if actual == expected:
        return
    else:
        print(actual,"not equal to", expected)
        raise Exception(actual,"looks like")

if __name__ == '__main__':
    equals(str(to_rope("abc")),"abc")
    equals(str(to_rope("abcde").substring(1,3).substring(1,1)),"c")
    assert str(to_rope("abcdefg").substring(1,3).substring(1,2).substring(1,1)) == "d"
