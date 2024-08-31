
class SuffixTreeNode:
    pass

class SuffixTree:
    def __init__(self, s):
        self.s = s
        self.root = self._build_tree()

    def _build_tree(self):
        pass

    def search(self, pattern):
        return True


def test_suffix_tree():
    tree = SuffixTree("banana$")
    assert tree.search("ana") == True
    assert tree.search("cdf") == False
    # assert tree.search("na$") == True
    # assert tree.search("") == True

def main():
    test_suffix_tree()