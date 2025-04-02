
def to_rope(s):
    return Rope(s)


class Rope:
    def __init__(self, s):
        self.s = s

    def __str__(self) -> str:
        return self.s

assert str(to_rope("abc")) == 'abc'