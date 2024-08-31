class Trie():
    def __init__(self) -> None:
        self.nodes = [None] * 26
        self.word = None
    
    def build_trie(self, words, cur):
        for w in words:
            for c in w:
                idx = ord(c) - ord('a')
                if not cur.nodes[idx]:
                    cur.nodes[idx] = Trie()
                cur = cur.nodes[idx]
        return cur

def test_trie():
    root = Trie()
    words = ["apple","aac"] 
    root.build_trie(words, root)
    print(root.nodes[0].nodes[0])


test_trie()