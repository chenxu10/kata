def decodeString(s):
    """
    # k is positive
    # input valid
    """
    
def test_decodeString():
    assert decodeString("3[a]2[bc]") == "aaabcbc"
    assert decodeString("3[bc1[a]]") == "bcabcabca"