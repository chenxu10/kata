









class Rope:
    def __init__(self, string):
        self.string = string
    
    def __str__(self):
        return self.string

def to_rope(x):
    return Rope("abc")

if __name__ == '__main__':
    assert str(to_rope("abc")) == "abc"