import pandas as pd

class Rope():
    def __init__(self, s) -> None:
        self.s = s
    def __str__(self):
        return self.s
def to_rope(s):
    return Rope(s)

def test_rope():
    assert str(to_rope("abc")) == "abc"


if __name__ == "__main__":
    test_rope()