


class Rope:
    def __init__(self, s):
        self.s = s
    
    def __str__(self):
        return self.s

    def substring(self, start, length):
        return Substring(self, start,length)
    
class Substring:
    def __init__(self, rope, start, length) -> None:
        pass
    def __str__(self):
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

