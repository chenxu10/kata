# TCR


# insert
# delete
# substring
# concatenate
# high level princples
# feelings

# API
def to_rope(s):
    return String(s)


class Rope:
    def substring(self, start, length):
        return Substring(self, start, length)

class String(Rope):
    def __init__(self,s):
        self.s = s

    def __str__(self):
        return self.s
    
class Substring(Rope):
    def __init__(self, rope, start, length):
        self.rope = rope
        self.start = start
        self.length = length

    def __str__(self) -> str:
        return str(self.rope)[self.start:self.start + self.length]
    


if __name__ == '__main__':
    assert str(to_rope("abc")) == "abc"
    assert str(to_rope("abcde").substring(1,3)) == "bcd"
    assert str(to_rope("abcde").substring(1,3).substring(1,1)) == "c"


