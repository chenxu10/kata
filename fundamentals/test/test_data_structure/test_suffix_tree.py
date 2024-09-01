class SuffixNode():
    def __init__(self) -> None:
        self.children = {}
        self.is_end = False

class SuffixTree():
    def __init__(self, s) -> None:
        self.s = s
        self.root = self._build_tree()

    def _build_tree(self):
        root = SuffixNode()
        
        for i in range(len(self.s)):
            self._insert_suffix(self.s[i:], root)

        return root
    
    def _insert_suffix(self, word, node):
        cur = node
        for c in word:
            if c not in cur.children:
                cur.children[c] = SuffixNode()
            cur = cur.children[c]
        cur.is_end = True
    
    def search(self, pattern):
        cur = self.root
        for c in pattern:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

def test_suffix_tree():
    s = "bananas"
    tree = SuffixTree(s)
    assert(tree.root.children["b"].is_end==False)
    assert(tree.search(s[2:]))

    # root._
    # assert root["b"].is_end == False
    # assert isinstance(root["b"].nodes, dict)
    # assert root.search("ananas") == True
    # assert root.search("nas") == False


if __name__ == "__main__":
    test_suffix_tree()