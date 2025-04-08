


class Rope:
    def __str__(self):
        return "abc"


def to_rope():
    return Rope("abcde")



def test_rope():
    assert str(to_rope("abcdec")) == "abc"



