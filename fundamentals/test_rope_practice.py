class Rope:
    def substring(self, start, length):
        return Substring(self, start, length)
    def concatenate(self, Rope):
        return Concatenate(self, Rope)

class Concatenate(Rope):
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right
        
    def __str__(self):
        return str(self.left) + str(self.right)

class String(Rope):
    def __init__(self, s):
        self.s = s
    
    def __str__(self):
        return self.s
    
    def delete(self, start, length):
        left = str(self.substring(0, start))
        right = str(self.substring(start + length, self.length() - start))
        return left + right
    
    def length(self):
        return len(self.s)
    
class Substring(Rope):
    def __init__(self,rope, start, length):
        self.rope = rope
        self.start = start
        self.leng = length
    
    def __str__(self):
        return str(self.rope)[self.start:self.start + self.leng]
    
    def length(self):
        return 3
 
def to_rope(x):
    return String(x)

# Testing framework
def equals(actual, expected):
    if actual == expected:
        return
    else:
        print(actual,"not equal to", expected)
        raise Exception("actual looks like", actual)

if __name__ == '__main__':
    ##
    equals(str(to_rope("abc")),"abc")
    equals(str(to_rope("abcde").substring(1,3).substring(1,1)),"c")
    assert str(to_rope("abcdefg").substring(1,3).substring(1,2).substring(1,1)) == "d"
    equals(str(to_rope("abc").concatenate(to_rope("de"))),"abcde")
    equals(to_rope("abcde").delete(1,3),"ae")
    #equals(to_rope("abcde").substring(1,3).length(),3)