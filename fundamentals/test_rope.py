# TODO

# insert
# delete
# substring
# concatenate

class Rope:
    def __init__(self,s):
        self.s = s

    def __str__(self):
        return self.s

    def substring(self, start, end):
        return Substring()
    
 
class Substring:
    def __str__(self):
        return "bcd"

def to_string(s):
    return Rope(s)

assert str(to_string("abc")) == "abc"
assert str(to_string("abcde").substring(1,3)) == "bcd"

##

####