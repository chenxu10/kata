class Trie:
    def __init__(self):
        self.nodes = [None] * 26
        self.word = None
    
    def build_word(self, word, cur):
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.nodes[idx]:
                cur.nodes[idx] = Trie()
            cur = cur.nodes[idx]
        return cur

def test_trie():
    t = Trie()
    cur = t.build_word('bc',t)
    print(cur.nodes[0])

def main():
    test_trie()
if __name__ == '__main__':
    main()
