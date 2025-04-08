


class Rope:
    def __init__(self, s):
        self.s = s
    
    def __str__(self):
        return self.s


def to_rope(s):
    return Rope(s)


def test_rope():
    assert str(to_rope("abcde")) == "abcde"

def main():
    test_rope()
    
if __name__ == '__main__':
    main()

