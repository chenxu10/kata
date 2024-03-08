









class Rope:
    def __init__(self, string):
        pass
    
    def __str__(self):
        return "abc"

def to_rope(x):
    return Rope("abc")

if __name__ == '__main__':
    assert str(to_rope("abc")) == "abc"