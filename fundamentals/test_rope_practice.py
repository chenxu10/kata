
# insert
# delete
# concatentae
# substring

# last rountine call
# trivial helper function
# test passes TCR




class Rope:
    def __init__(self,s):
        self.s = s

    def __str__(self):
        return self.s 

def to_string(s):
    return Rope(s) 

assert str(to_string("abc")) == "abc"



### "abc", "def", 2, 5 --> "cde"





