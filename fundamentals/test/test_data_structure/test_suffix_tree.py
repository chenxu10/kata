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
        for c in word:
            if c not in node.children:
                node.children = SuffixNode()
            node.childeren = node.children[c]
        node.is_end = True
        return node
    
    def search(self, pattern):
        for c in pattern:
            if c not in self.root.children:
                return False
        return True

def test_suffix_tree():
    s = "bananas"
    root = SuffixTree(s)
    assert root["b"].is_end == False
    assert isinstance(root["b"].nodes, dict)
    assert root.search("ananas") == True
    assert root.search("nas") == False
