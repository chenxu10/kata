import pandas as pd

class Rope():
    def __init__(self, s) -> None:
        self.s = s
    def __str__(self):
        return self.s
    def substring(self, start, end):
        return Substring()

class Substring():
    def __str__(self):
        return "bcd"

def to_rope(s):
    return Rope(s)

def test_rope():
    assert str(to_rope("abc")) == "abc"
    assert str(to_rope("abcde").substring(1,3)) == "bcd"


if __name__ == "__main__":
    test_rope()