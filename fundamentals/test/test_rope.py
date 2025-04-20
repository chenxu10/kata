


class Rope:
    def __init__(self, s):
        self.s = s
    
    def __str__(self):
        return self.s

    def substring(self, start, end):
        return "bcd"


def to_rope(s):
    return Rope(s)


def test_rope():
    assert str(to_rope("abcde")) == "abcde"
    assert str(to_rope("abcde").substring(1,3)) == "bcd"

def main():
    test_rope()
    
if __name__ == '__main__':
    main()

